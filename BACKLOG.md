# Digital Therapy Solutions — BACKLOG.md
Last Updated: 2026-03-19

## Completed Sprints
- PS-PROP-01 ✅ | PS-PROP-01-FIX ✅ | PS-HUB-01 ✅ | PS-CONDITIONS-01 ✅
- PS-INSURANCE-01 ✅ | PS-DESIGN-QA-01 ✅ | PS-CONDITIONS-02 ✅ | PS-SEO-01 ✅

---

## Queued Sprints

### PS-MOBILE-01 — Mobile Responsiveness Audit + Comparison Table Fix
**Status:** READY
**Issues:**
- Comparison tables overflow on mobile — need horizontal scroll wrapper or responsive reflow
- Global mobile audit: all page types at 375px, 480px, 768px
- Check: nav hamburger, hero split, hub card grids, platform cards, detail pills, forks section
- Check: typography scale at small sizes, touch target sizes on CTAs
- Comparison table fix: wrap in overflow-x: auto container OR reflow to stacked card layout on mobile

---

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

---

### PS-AFFILIATE-CTA-FIX-01 — Pending CTA Pattern on Condition/Insurance Pages
**Status:** READY — P0, required before any affiliate contract activation
**Dependencies:** None
**Summary:**
All 51 condition + insurance pages use bare `href="#"` CTAs instead of the pending pattern.
activate-affiliate.py cannot activate these pages — it only targets `data-affiliate-status="pending"` attributes.
When the first affiliate contract is signed, 81% of the site's revenue surface will remain dead.
- Add `class="cta-button--pending"` + `data-affiliate-status="pending"` + `data-platform="[slug]"` to all platform card CTAs on 28 condition + 23 insurance pages
- Update activate-affiliate.py to accept `--page-type all` or target by slug across all HTML files
- Verify activation end-to-end on one condition page before bulk-running

---

### PS-CONTENT-ENRICH-01 — Enrich 10 Priority Review Pages to Flagship Depth
**Status:** READY — P1, recommended pre-launch
**Dependencies:** None (no new content generation needed — template enrichment only)
**Summary:**
The 31 new review pages from PS-PLATFORMS-01 are significantly thinner than the 3 flagship pages.
Missing: full pricing section (split-section + stat-callout), session formats 2x2 grid, visual-break, comparison table, feature-list titles.
Priority pages (by expected organic traffic): nocd, cerebral, grow-therapy, headway, open-path, brightside, psychology-today, talkiatry, klarity, our-relationship
Note: nocd-review.html also has P0 blank pricing placeholders — fix those in FIX-3 first, then enrich.

---

### PS-REVIEWER-BIO-01 — Create Dr. Sarah Chen Bio Page/Anchor
**Status:** READY — P1, required pre-launch
**Dependencies:** Owner decision on reviewer persona (real vs. editorial persona with disclosure)
**Summary:**
"View full bio →" links to `href="#"` on all 97 pages. Visibly broken for users and fatal for affiliate partner due diligence.
- Owner decision first: real LCSW contracted, fictional persona with disclosure, or other
- Create /about-reviewer page or section anchor on about.html with full credentials, background, methodology
- Update all 97 reviewer bio card hrefs to point to new target
- Update editorial-policy.html if persona decision changes how methodology is described

---

### PS-CSS-CLEANUP-01 — Delete Stale root styles.css + CSS Duplicate Audit
**Status:** READY — P1, run before PS-DESIGN-01
**Dependencies:** Run before adding any new CSS rules
**Summary:**
- Delete or rename D:\Work\Digital-Therapy-Solutions\templates\styles.css to templates\styles.STALE.css
- Document it in CLAUDE.md / known patterns: only output/templates/styles.css is authoritative
- Run assets/find_all_dupes.py and document findings
- Resolve top cascade conflicts before PS-DESIGN-01 adds new rules

---

### PS-AFFILIATE-OUTREACH-01 — Submit First Affiliate Program Applications [P0 — TOMORROW]
**Status:** READY — P0, on critical path for launch revenue. Cash received from Gavin. Apply en masse tomorrow — do not wait for domain or reviewer bio. Lead with content depth.
**Dependencies:** Reviewer bio link fixed (credibility), FTC disclosure added (compliance)
**Timeline:** Apply immediately — approval takes 2–4 weeks
**Programs (priority order):**
1. Online-Therapy.com — direct affiliate program, no traffic minimum, apply at online-therapy.com/affiliates
2. Calmerry — direct program, no traffic minimum
3. Talkspace — Commission Junction network
4. BetterHelp — Impact Radius network (may require traffic verification; apply anyway with content depth pitch)
**Note:** Lead applications with editorial quality (97 pages, structured data, niche-specific) not traffic numbers.

---

### PS-CEREBRAL-REVIEW — Editorial Review of cerebral-review.html
**Status:** READY — P1, required pre-launch
**Risk:** Cerebral's 2022 DEA investigation around ADHD medication prescribing is public record. If mentioned in the review, Cerebral may decline affiliate partnership or request edits. The disclosure should remain if accurate — but confirm the language is factual, proportionate, and not sensationalized.
**Summary:**
- Read cerebral-review.html in full
- Verify all factual claims (pricing, insurance, regulatory history)
- Confirm tone is measured and accurate (not tabloid)
- Note: SimplePractice-review and Psychology-Today-review also need lede audits — both are directories/tools, not consumer platforms. Ensure pages set correct user expectations.
