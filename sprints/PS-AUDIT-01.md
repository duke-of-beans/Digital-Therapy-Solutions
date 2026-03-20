Execute Sprint PS-AUDIT-01 — Full Site Audit for Digital Therapy Solutions.
Multi-hat inspection: Designer / Engineer / DTS Owner / Affiliate Partner.

Read these files FIRST before doing anything:
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\STATUS.md
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\BACKLOG.md
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\templates\styles.css
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\index.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\betterhelp-review.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\aetna.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\conditions.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\reviews.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\insurance.html

Summary: Produce a comprehensive multi-perspective audit report for DTS as a living
document. The site has 97 pages across 5 verticals, is SEO-hardened, and is
pre-launch pending domain + affiliate contracts. This audit surfaces everything that
is not easily visible from casual review — technical debt, design inconsistencies,
SEO gaps, content quality issues, and affiliate readiness — organized by role.

---

AUDIT METHODOLOGY

Do NOT fix anything in this sprint. Observe, document, and triage.
Every finding goes into the report with a severity and recommended action.
Severity tiers:
  P0 — Blocks launch or revenue. Fix before going live.
  P1 — Degrades user experience or SEO measurably. Fix soon.
  P2 — Polish and improvement. Fix when possible.
  P3 — Nice to have. Backlog.

Findings that are FIX NOW candidates (small, surgical, safe) are flagged separately
at the end of the report for immediate execution in a follow-up session.

---

HAT 1 — DESIGNER

Audit lens: visual coherence, typography hierarchy, spacing rhythm, icon system,
logo treatment, color application, mobile responsiveness, component consistency.

Check:
1. Typography — scan 8 pages across all types (homepage, condition, insurance, review,
   hub, legal, supporting, 404). Is Fraunces used correctly as personality font?
   Is DM Mono confined to pricing/data only? Is Instrument Serif italic used only
   for editorial accent moments? Flag any violations.

2. Icon system — conditions.html hub has the stroke SVG system. Is it applied
   consistently? Are there any remaining emoji or incompatible icons anywhere?
   Check index.html condition tiles, conditions.html, individual condition pages.

3. Logo treatment — all logos should be max 64px on cards, object-fit: contain,
   --bg-secondary fill. Check: reviews.html hub cards, insurance.html hub cards,
   index.html insurance tiles, affordable.html platform cards. Flag any that
   still look wrong.

4. Color application — --accent-primary (teal) for CTAs/links, --accent-warm
   (terracotta) for human signal moments. Flag any hardcoded hex colors in HTML
   that should use CSS variables.

5. Spacing rhythm — do pages feel consistent? Are there sections that feel cramped
   or too airy vs the established rhythm? Note any outlier pages.

6. Mobile — mentally model the 4-column hub grid at 480px (2-col), the hero split
   at mobile (stacked), the nav hamburger. Flag any known breakpoint issues.

7. Component consistency — verdict-box, pull-quote, feature-list, split-section,
   stat-callout, timeline-list. Are these applied on all 6 target detail pages?
   Do they look consistent across pages?

8. 404 page — does it match site design? Does it have a useful fork?

---

HAT 2 — ENGINEER

Audit lens: HTML validity, CSS health, JS reliability, routing, performance,
SEO technical layer, build process integrity.

Check:
1. CSS health — run assets/find_all_dupes.py. Document all remaining duplicate
   selectors. Flag any that could cause cascade conflicts.

2. Stylesheet divergence — templates/styles.css and output/templates/styles.css
   are diverged. Document which is authoritative and flag the risk of future
   confusion. Recommend resolution.

3. Routing — test 5 clean URLs live on Vercel:
   /reviews, /conditions, /insurance, /betterhelp-review, /anxiety
   Confirm all return 200 and render correctly. Test /nonexistent → 404.html.

4. Asset paths — with outputDirectory set to output/, ../assets/ paths from output/
   pages resolve to /assets/ which is served from output/assets/. Confirm this is
   working for logos, hero images, branding. Note any 404s.

5. SEO layer — spot-check 3 pages for: canonical tag, BreadcrumbList JSON-LD,
   FAQPage JSON-LD (condition/insurance), Review JSON-LD (review pages).
   Confirm sitemap.xml is accessible at /sitemap.xml. Confirm robots.txt at /robots.txt.

6. Internal links — do all footer Quick Links point to hub pages (not detail pages)?
   Do breadcrumbs work correctly across page types?

7. Pending CTA system — confirm data-affiliate-status="pending" is on all 31 new
   platform review pages. Confirm activate-affiliate.py exists and is documented.

8. Python scripts — assets/ has many build/patch scripts. Are any likely to fail
   on re-run? Are any now redundant? Flag any that modify output/ files and could
   cause conflicts if run again.

9. Build integrity — is there a risk of re-running any assembly script that would
   overwrite the manually-patched output/ files? Document the risk.

---

HAT 3 — DTS OWNER

Audit lens: content quality, editorial integrity, affiliate readiness, launch
checklist, revenue surface, competitive position.

Check:
1. Content quality — read the full body text of 5 pages: betterhelp-review.html,
   aetna.html, anxiety.html, nocd-review.html, life-transitions.html.
   Is the voice consistent? Is it "informed ally"? Does it name feelings before
   solutions? Is pricing specific? Are there any marketing clichés or deny-words
   (affordable, cheap, best, amazing, trusted by thousands)?

2. Platform data accuracy — are the pricing figures, insurance claims, and platform
   descriptions on the 31 new review pages accurate and specific? Or are they
   vague/generic? Flag the 5 weakest pages by content quality.

3. Reviewer credibility — "Dr. Sarah Chen, LCSW" appears across all pages. Is this
   consistent? Is the reviewer bio present on all detail pages? Is the editorial
   policy page coherent?

4. Affiliate readiness — list all 34 platforms and their current CTA status:
   - 3 pages have "pending" CTAs (betterhelp, talkspace, online-therapy-com retrofitted)
   - 31 new pages have "pending" CTAs
   Confirm the activate-affiliate.py workflow is documented for the owner.

5. Launch checklist — what remains before go-live?
   - Domain (Gavin) — status unknown
   - GSC property creation and sitemap submission
   - Editorial reviewer onboarding
   - Affiliate applications (which programs, which networks?)
   - Any legal/compliance gaps?

6. Revenue surface — how many affiliate entry points does the site have?
   Count: CTA buttons across all 34 review pages + cross-links from condition/
   insurance pages. Estimate total clickable affiliate surfaces.

7. Competitive gap — what does ChoosingTherapy or HelpGuide have that DTS doesn't?
   What does DTS have that they don't? Note 3-5 genuine advantages.

---

HAT 4 — AFFILIATE PARTNER

Audit lens: what a platform (BetterHelp, Talkspace, etc.) sees when they evaluate
DTS for affiliate partnership. Trust signals, traffic potential, content quality,
disclosure compliance.

Check:
1. Trust signals — does the site look like a legitimate editorial operation?
   Editorial policy page: does it explain methodology clearly?
   Affiliate disclosure page: is it prominent, honest, and compliant?
   Reviewer credentials: are they believable?

2. Content fairness — do the reviews feel honest or promotional? Would a platform
   be comfortable being reviewed here even if they got a 3.7/5?
   Check cerebral-review.html — it notes regulatory history. Is that too harsh?
   Check simplepractice-review.html — it explains SimplePractice isn't a marketplace.
   Is that accurate and fair?

3. Disclosure compliance — is the affiliate disclosure linked from every page footer?
   Is it referenced in-page on review pages? FTC requires disclosure near the
   affiliate link, not just in a footer. Flag any pages missing inline disclosure.

4. Traffic potential signals — a partner evaluating DTS will look at:
   - Domain age/authority (pre-launch, so low — note this)
   - Content depth (97 pages, structured — note this)
   - SEO readiness (sitemapped, structured data — note this)
   - Niche specificity (online therapy only — strong signal)
   Flag any content that looks thin or auto-generated vs genuinely editorial.

5. Platform-specific concerns — for each of the 34 platforms, is the page accurate
   enough that the platform wouldn't object? Flag the 3 riskiest pages.

---

TASK: Produce the audit report

Write the report to:
  D:\Work\Digital-Therapy-Solutions\PS-AUDIT-01-REPORT.md

Structure:
  # DTS Site Audit — PS-AUDIT-01
  Date: [today]
  Auditor: Claude (4 hats)
  Site: digital-therapy-solutions.vercel.app
  Pages audited: 97

  ## Executive Summary
  [3-5 sentences. What is the overall health? What are the top 3 concerns?
  What is the launch readiness verdict?]

  ## Hat 1 — Designer Findings
  [All findings, each with: Finding | Severity | Recommended Action]

  ## Hat 2 — Engineer Findings
  [Same format]

  ## Hat 3 — DTS Owner Findings
  [Same format]

  ## Hat 4 — Affiliate Partner Findings
  [Same format]

  ## FIX NOW Queue
  [Items that are P0/P1 AND fixable in <3 tool calls. List with exact fix.]

  ## Backlog Additions
  [New items to add to BACKLOG.md with sprint designation]

  ## Launch Readiness Checklist
  [Complete checklist: what's done, what's blocking, what's optional]

---

<!-- phase:execute -->

After the report is written:
1. Add any new backlog items to D:\Work\Digital-Therapy-Solutions\BACKLOG.md
2. Update STATUS.md: add PS-AUDIT-01 ✅ COMPLETE
3. Write MORNING_BRIEFING.md
4. Commit: audit(site): PS-AUDIT-01 — full multi-hat site audit report
5. Push

---

CRITICAL CONSTRAINTS:
- DO NOT fix issues during this sprint — document only
- Exception: FIX NOW queue items may be executed AFTER the report is written
- Every finding needs a severity (P0/P1/P2/P3)
- Be genuinely critical — this is a pre-launch inspection, not a celebration
- The affiliate partner hat should be the most skeptical voice in the report
