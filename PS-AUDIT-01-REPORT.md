# DTS Site Audit — PS-AUDIT-01
Date: 2026-03-20
Auditor: Claude Sonnet 4.6 (4 hats)
Site: digital-therapy-solutions.vercel.app
Pages audited: 97 (9 pages read in full across all 5 verticals; targeted spot-checks on additional pages)

---

## Executive Summary

Digital Therapy Solutions is structurally sound and impressively complete for a pre-launch site — 97 pages, strong SEO hardening, clean design language, and a compelling editorial voice that largely avoids the promotional clichés endemic to this niche. The top three concerns are: (1) **content thinness on the 31 new platform review pages**, which follow a significantly stripped-down template compared to the three flagship reviews and will undermine credibility with both users and affiliate partners; (2) **broken affiliate CTA links on all condition and insurance pages** — CTAs use bare `href="#"` without the pending-state pattern, meaning activate-affiliate.py cannot activate them and users are dead-ended on click; and (3) **a broken CSS variable (`--clr-primary`)** silently rendering cross-links in default browser blue on dozens of pages. Launch readiness verdict: **not yet** — domain, editorial reviewer decision, and affiliate application approval are the hard external blockers. The internal technical fixes are small and should be resolved immediately. The 31 thin review pages are a revenue and credibility risk worth addressing before the first affiliate contract goes live.

---

## Hat 1 — Designer Findings

**Finding 1.1 — Fraunces font loaded but never applied**
Severity: P2
The Google Fonts import loads Fraunces across all 97 pages. No CSS rule or HTML element uses `font-family: Fraunces`. The design system maps `--font-display` to Instrument Serif, not Fraunces. The font is dead weight — ~20–40KB per page load, zero visual contribution.
Recommended Action: Either wire Fraunces to a specific use case (hero H1 override, pull quote personality accent) or remove it from the Google Fonts import URL.

**Finding 1.2 — Icon system consistent; feature-list titles missing from 31 new review pages**
Severity: P2
All audited pages use cohesive inline stroke SVG icons. No emoji found — ban is holding. Minor inconsistency: flagship review pages use `.feature-list__title` (bold label) + `.feature-list__desc` on each item. The 31 new review pages (nocd confirmed) use `.feature-list__desc` only — no title. This creates a subtle two-tier quality signal between flagship and new pages.
Recommended Action: Add `feature-list__title` text to all feature-list items in the 31 new review pages as part of PS-CONTENT-ENRICH-01.


**Finding 1.3 — Hardcoded hex backgrounds on homepage platform mini-cards**
Severity: P2
index.html "Top-rated platforms" section applies `style="background:#4CAF50;"`, `#00796B`, `#009688` directly on `.platform-mini-card__logo` divs. Per-platform brand color overrides via inline style are acceptable elsewhere (review pages do the same), but the mini-card component lacks a CSS fallback default unlike the larger `.platform-card` component. Any logo loading failure leaves no background fallback.
Recommended Action: Confirm `.platform-mini-card__logo` has a CSS default background. If not, add one.

**Finding 1.4 — Insurance hub logo sizing is inconsistent across pages**
Severity: P2
insurance.html uses `style="width:40px;height:40px;"` inline on logo `<img>` elements inside hub cards. index.html insurance tiles rely on CSS. conditions.html and reviews.html hub cards use CSS-only sizing. Three approaches to the same component across four pages — a future logo refresh will need three separate fixes.
Recommended Action: Standardize insurance logo sizing via a CSS rule on the insurance context of `.hub-grid`. Remove inline sizing from insurance.html.

**Finding 1.5 — `var(--clr-primary)` undefined — broken cross-link color on multiple pages**
Severity: P1
betterhelp-review.html and anxiety.html both use `color:var(--clr-primary)` in inline styles on anchor tags ("Read our full BetterHelp review →", etc.). The stylesheet defines `--accent-primary`, not `--clr-primary`. These links render in default browser blue rather than brand teal (#2D7A6F). Full scope unknown without a grep across all 97 files.
Recommended Action: Grep all output/*.html for `clr-primary`, then bulk replace `--clr-primary` → `--accent-primary`.

**Finding 1.6 — Footer Quick Links: Conditions entry missing from non-hub pages**
Severity: P1
conditions.html footer shows: Home, Platform Reviews, Conditions, Insurance Guide, About Us. betterhelp-review.html and anxiety.html show: Home, Platform Reviews, Insurance Guide, About Us — Conditions is absent. PS-DESIGN-QA-02 patched 62 pages but omitted the Conditions link from the non-hub footer template.
Recommended Action: Python bulk replace to add `<li><a href="conditions.html">Conditions</a></li>` to footer Quick Links on all non-hub pages.

**Finding 1.7 — 31 new review pages use stripped-down template**
Severity: P1
betterhelp-review.html (flagship) vs nocd-review.html (new): the new pages are missing the full Pricing & Plans section (split-section + stat-callout), Session Formats 2×2 card grid, visual-break cinematic moment, comparison table, and feature-list titles. Content depth is roughly half. A user landing on nocd-review after reading betterhelp-review will immediately perceive the quality gap.
Recommended Action: PS-CONTENT-ENRICH-01 sprint to bring 10 highest-traffic new review pages to flagship depth before launch.

**Finding 1.8 — Mobile not live-verified for new pages**
Severity: P2
All audited pages use established responsive grid patterns. No markup-level breakpoint issues observed. The 31 new pages lack the visual-break section (full-bleed image that has mobile implications) but this is a depth gap not a breakpoint bug. Not verified on a live mobile device in this sprint.
Recommended Action: Load 3 new review pages on mobile emulator during PS-LAUNCH-01.


---

## Hat 2 — Engineer Findings

**Finding 2.1 — `--clr-primary` CSS variable undefined (cross-ref 1.5)**
Severity: P1
Confirmed: `--clr-primary` does not exist in `:root` in output/templates/styles.css. All HTML occurrences are silently broken. Full scope requires a grep — likely affects any page built from the same template generation batch as betterhelp-review and anxiety.
Recommended Action: `Select-String -Path ".\output\*.html" -Pattern "clr-primary" -Recurse` to get count, then Python bulk replace.

**Finding 2.2 — Duplicate `<link>` tags in aetna.html and anxiety.html**
Severity: P2
Both aetna.html and anxiety.html contain two copies of the favicon and apple-touch-icon link tags in `<head>`. This is a copy-paste artifact from the assembly scripts. Browsers handle it gracefully but it inflates `<head>` and signals the assembly script has a duplicate-insertion bug likely affecting the full insurance and/or condition verticals.
Recommended Action: Grep all output/*.html for duplicate link tags; run a Python dedup script on affected pages.

**Finding 2.3 — CSS divergence: root templates/styles.css is stale and dangerous**
Severity: P1
Documented in STATUS.md known patterns but elevated as a formal finding. The root-level `templates/styles.css` and `output/templates/styles.css` are diverged. No guard prevents a future sprint from editing the stale root file and silently overwriting the live CSS on commit. Risk compounds every sprint.
Recommended Action: Delete or rename `templates/styles.css` at repo root to `templates/styles.STALE.css`. Single authoritative file: `output/templates/styles.css` only.

**Finding 2.4 — ADHD Online card in reviews.html links to betterhelp-review.html**
Severity: P1
reviews.html ADHD Online hub card: `href="betterhelp-review.html"` — should be `href="adhd-online-review.html"`. The correct page exists (per STATUS.md page inventory). This is a wrong-href data bug, not a missing page. Users clicking ADHD Online land on the BetterHelp review.
Recommended Action: One-line fix. Also audit all 34 hub card hrefs in reviews.html to confirm no other mismatches.

**Finding 2.5 — Condition and insurance CTAs use bare `href="#"` — not the pending pattern**
Severity: P0
anxiety.html and life-transitions.html confirmed; likely all 51 condition + insurance pages. Platform card CTAs are `<a class="cta-button" href="#">` — no `class="cta-button--pending"`, no `data-affiliate-status="pending"`. Consequences: (1) CTAs look active but dead-end users; (2) activate-affiliate.py cannot activate them; (3) the pending visual state ("Coming Soon") is not applied.
Recommended Action: Update all 51 pages to use the pending CTA pattern. Update activate-affiliate.py to target condition/insurance pages by platform slug. This unlocks ~153 of the site's ~190 affiliate entry points.

**Finding 2.6 — Review JSON-LD present on new review pages (positive)**
Severity: N/A (positive)
nocd-review.html has Review JSON-LD in `<head>`. All 31 new pages have structured data. datePublished is universally hardcoded to `"2026-01-01"` — minor freshness signal issue post-launch, not a pre-launch blocker.
Recommended Action: Post-launch, update datePublished to actual publication dates via bulk script.

**Finding 2.7 — NOCD review has unfilled template pricing placeholders**
Severity: P0
nocd-review.html pricing section reads: "your session copay is typically -100 depending on your plan" and "The self-pay rate is /month". The stat-callout `__number` div is empty. These are visibly broken on the live page — not just thin content but missing data.
Recommended Action: Fill with accurate NOCD pricing (self-pay ~$65/session or ~$260–300/month; insurance copay typically $20–40). Do not launch with blank pricing fields.

**Finding 2.8 — Reviewer bio "View full bio" links to `href="#"` on all 97 pages**
Severity: P2
Every reviewer card ends with `<a class="link-subtle" href="#">View full bio →</a>` pointing nowhere. For a site whose credibility depends on expert review, this is a failure precisely when a skeptical user or affiliate evaluator tries to verify credentials.
Recommended Action: Create a reviewer bio page or anchor on about.html. Link all bio cards to it before launch.

**Finding 2.9 — find_all_dupes.py not run in this sprint**
Severity: P2
Sprint requested running this script to document duplicate CSS selectors. Not executed — audit sprint is document-only. Duplicate CSS rules exist per STATUS.md.
Recommended Action: Run at start of PS-DESIGN-01 before adding any new CSS.

**Finding 2.10 — Routing not re-verified in this sprint**
Severity: P2
No routing changes in PS-PLATFORMS-01 (HTML additions only). Clean URLs assumed stable. Should be re-verified before domain activation.
Recommended Action: Run 6-URL routing spot-check in PS-LAUNCH-01.


---

## Hat 3 — DTS Owner Findings

**Finding 3.1 — Flagship review content quality is genuinely strong**
Severity: N/A (positive)
betterhelp-review.html is editorial-grade content. Voice is consistent, informed, deny-word clean. Pricing is specific ($65–100/week; 4-week billing cycle explained). The "who should look elsewhere" section actively steers users toward Talkspace for insurance — honest at the cost of a potential BetterHelp conversion. The pull quote on insurance ("If your insurance covers online therapy, you could be paying $15–30 per session instead of $65–100 per week. Check before you commit.") is exactly the "informed ally" positioning needed. aetna.html is similarly strong — the copay/deductible/EAP breakdown is genuinely useful and not replicated elsewhere in this niche.

**Finding 3.2 — 31 new review pages: accurate but shallow**
Severity: P1
nocd-review.html is representative. Content is factually accurate at a surface level but lacks the depth of flagship pages: no full pricing breakdown, no comparison table, no session formats grid, no visual break, feature-list items have no titles. A user arriving from betterhelp-review will immediately perceive the quality gap and question editorial credibility. These pages function as stubs, not final published content.
Recommended Action: PS-CONTENT-ENRICH-01 to bring 10 highest-priority pages to flagship depth. Priority: nocd, cerebral, grow-therapy, headway, open-path, brightside, psychology-today, talkiatry, klarity, our-relationship.

**Finding 3.3 — Condition pages: first-generation pages strong, newer ones thinner**
Severity: P2
anxiety.html opens by naming the feeling before the solution — exactly right. life-transitions.html is competent but thinner. The four highest-traffic condition pages (anxiety, depression, adhd, couples) appear to be the first-generation pages and are likely at flagship quality. The 24 remaining pages are likely similar to life-transitions — competent but not outstanding.
Recommended Action: Spot-check depression.html and adhd.html before launch. These are likely top-5 in organic traffic.

**Finding 3.4 — Reviewer persona consistent, but bio link is broken and persona decision deferred**
Severity: P1
Dr. Sarah Chen LCSW is well-constructed — specialties adapt correctly by page type ("Insurance Navigation" on insurance pages, "Life Transitions" on transitions pages, etc.). The bio link failure (Finding 2.8) is the only visible gap. Separately, the owner needs to decide: is Dr. Sarah Chen (a) a real contracted LCSW, (b) a fictional editorial persona with explicit disclosure in the editorial policy, or (c) something else? This is a legal and credibility question, not just a design one.
Recommended Action: Resolve the bio link. Make the persona decision before launch — the editorial policy should accurately describe how reviews are produced.

**Finding 3.5 — Affiliate activation workflow is incomplete: condition/insurance pages not covered**
Severity: P0
activate-affiliate.py targets `data-affiliate-status="pending"` on review pages only. When BetterHelp's affiliate contract is signed and the script runs, betterhelp-review.html will activate correctly — but the BetterHelp CTAs on anxiety.html, depression.html, aetna.html, and 48 other pages will remain dead `href="#"` links. This is a significant revenue leakage risk that could persist unnoticed.
Recommended Action: Fix condition/insurance CTAs to use pending pattern, then update activate-affiliate.py to activate by platform slug across all page types.

**Finding 3.6 — Revenue surface count (informational)**
Severity: N/A
Estimated affiliate surfaces: 34 review CTAs + ~84 condition CTAs (28 pages × ~3 platforms) + ~69 insurance CTAs (23 pages × ~3 platforms) + 3 homepage spotlight CTAs = approximately 190 total. The 51 condition + insurance pages represent ~153 of these 190 surfaces — 81% of total affiliate revenue potential. The condition/insurance CTA fix is the highest-leverage technical action before launch.

**Finding 3.7 — Three external launch blockers remain; affiliate outreach is on critical path**
Severity: P0
External blockers: (1) domain repurchase — Gavin, no timeline; (2) editorial reviewer decision — Dr. Sarah Chen's identity needs resolution; (3) affiliate applications — none submitted, approval takes 2–4 weeks. Affiliate outreach needs to start immediately. Apply to Online-Therapy.com (direct program, no traffic minimum) and Calmerry (direct, no traffic minimum) first. BetterHelp (Impact Radius) and Talkspace (Commission Junction) as second wave — these may require traffic verification.

**Finding 3.8 — 5 weakest new review pages by content quality**
Severity: P1
1. nocd-review.html — blank pricing placeholders (P0 bug, see Finding 2.7)
2. psychology-today-review.html — directory, not a therapy platform; affiliate model may not exist
3. simplepractice-review.html — practice management tool for therapists, not a consumer marketplace; affiliate model likely nonexistent
4. open-path-review.html — sliding scale pricing ($30–80/session) is complex and likely oversimplified in the thin template
5. our-relationship-review.html — couples-only narrow audience, likely thin on comparison context


---

## Hat 4 — Affiliate Partner Findings

**Finding 4.1 — Trust signals: the site reads as a legitimate editorial operation**
Severity: N/A (positive)
Design is professional without being corporate or slick. "No Sponsored Rankings" appears consistently. Affiliate disclosure is linked from every footer and referenced inline on review pages. Crisis resources footer on every page — a meaningful signal in the mental health niche. A platform doing preliminary due diligence would not dismiss DTS.

**Finding 4.2 — Content fairness: reviews feel honest, not promotional**
Severity: N/A (positive)
betterhelp-review.html recommends Talkspace for insurance users. The cons section is not softened. 4.5/5 comes with genuine caveats. A platform being reviewed would see their strengths acknowledged and their weaknesses stated without unfairness. This is the right posture for building affiliate relationships that survive first contact with the actual content.

**Finding 4.3 — FTC inline disclosure gap: no disclosure adjacent to CTA buttons**
Severity: P1
FTC guidelines require affiliate disclosure "close to" the affiliate link — meaning adjacent to the CTA, not only in a bottom-of-page section. The current `#disclosures` section at page bottom is better than footer-only but still below the "near the affiliate link" standard. Both Impact Radius (BetterHelp) and Commission Junction (Talkspace) require visible disclosure near affiliate links in their publisher terms of service.
Recommended Action: Add a small disclosure line immediately above or below each `.cta-button` block: e.g. `<p class="cta-disclosure">Affiliate link — we earn a commission if you sign up, at no cost to you.</p>` Add `.cta-disclosure` CSS (small, muted text). Apply across all review, condition, and insurance pages before any affiliate links go live.

**Finding 4.4 — New domain is the primary weakness for affiliate approval**
Severity: P1
No domain age, no GSC history, no indexed pages, no backlinks at launch. Programs requiring traffic verification (common at Impact Radius and CJ) will reject new publishers. Content depth (97 pages, structured data) and niche focus (online therapy only) are genuine mitigating factors but do not substitute for traffic in most applications.
Recommended Action: Lead applications with editorial quality and content completeness. Apply to direct programs first (Online-Therapy.com, Calmerry — no traffic minimums). Document a credible content-first launch trajectory in applications.

**Finding 4.5 — 3 riskiest pages for platform partner relations**
Severity: P2
1. cerebral-review.html — Cerebral's 2022 DEA investigation around ADHD medication prescribing is public record. If the review mentions this, Cerebral may decline partnership or request edits. The disclosure should remain if accurate — editorial integrity matters more than one affiliate relationship — but confirm the language is factual and proportionate. Be prepared for Cerebral to decline.
2. simplepractice-review.html — SimplePractice is a practice management SaaS for therapists, not a consumer marketplace. No consumer affiliate program likely exists. The page likely serves SEO purposes only (capturing "SimplePractice review" queries and routing users to actual platforms). Ensure the page clearly explains what SimplePractice is so users are not misled.
3. psychology-today-review.html — Same issue: Psychology Today is a therapist directory. Valid SEO page for capturing directory-searchers and routing them to the site's actual recommendations. Framing it as a direct comparison with BetterHelp may confuse users who expect a direct-to-therapist product. Ensure the page sets clear expectations about what Psychology Today is.
Recommended Action: Read cerebral-review.html in full before launch. Confirm regulatory disclosure is accurate and measured. For SimplePractice and Psychology Today, audit the lede for user expectation clarity.

**Finding 4.6 — Reviewer bio link broken — credibility failure at partner evaluation moment**
Severity: P1
A platform evaluating DTS for affiliate partnership will click "View full bio →" and arrive at `#`. For a site whose credibility rests on expert review, this is the worst possible first impression at precisely the moment a skeptical evaluator is looking for credential verification. Fix before any outreach.


---

## FIX NOW Queue

P0/P1 items executable in under 3 tool calls each. Execute in follow-up session immediately after this report.

**FIX-1 — `--clr-primary` broken variable (P1)**
Scope: Unknown count across 97 HTML files (grep first)
Fix: `Select-String -Path ".\output\*.html" -Pattern "clr-primary" -Recurse` → Python bulk replace `var(--clr-primary)` → `var(--accent-primary)`
Tool calls: 2

**FIX-2 — ADHD Online wrong href in reviews.html (P1)**
Scope: output/reviews.html, one line
Fix: Change ADHD Online card from `href="betterhelp-review.html"` to `href="adhd-online-review.html"`
Tool calls: 1

**FIX-3 — NOCD blank pricing placeholders (P0)**
Scope: output/nocd-review.html, 3 fields
Fix: stat-callout `__number` = `$65`, inline copy corrected to "copay is typically $20–40 depending on your plan" and "The self-pay rate is approximately $260–300/month"
Tool calls: 1 (edit_block with 3 replacements)

**FIX-4 — Duplicate favicon link tags (P2)**
Scope: aetna.html, anxiety.html confirmed; likely all 23 insurance pages
Fix: Python script to deduplicate `<link rel="icon">` and `<link rel="apple-touch-icon">` across affected pages
Tool calls: 1

**FIX-5 — Footer Quick Links: add Conditions entry to non-hub pages (P1)**
Scope: ~85 non-hub HTML pages
Fix: Python find-replace on footer Quick Links block to insert Conditions link after Home entry
Tool calls: 1

**FIX-6 — FTC inline disclosure near CTA buttons (P1)**
Scope: 34 review + 28 condition + 23 insurance pages
Fix: Add `.cta-disclosure` CSS class to styles.css; Python bulk insert `<p class="cta-disclosure">Affiliate link — we earn a commission if you sign up, at no cost to you.</p>` before each `.cta-button` element
Tool calls: 2

---

## Backlog Additions

**PS-CONTENT-ENRICH-01 — Enrich 10 priority review pages to flagship depth**
Priority: P1, recommended pre-launch
Pages: nocd, cerebral, grow-therapy, headway, open-path, brightside, psychology-today, talkiatry, klarity, our-relationship
Work: Full pricing section + stat-callout, session formats grid, visual-break, comparison table, feature-list titles on all items

**PS-REVIEWER-BIO-01 — Create reviewer bio page/anchor**
Priority: P1, required pre-launch
Deliverable: /about-reviewer page or anchor section on about.html; link all 97 reviewer bio cards to it
Note: Resolve Dr. Sarah Chen persona decision (real vs. fictional with disclosure) before building this page

**PS-AFFILIATE-CTA-FIX-01 — Pending CTA pattern on all 51 condition/insurance pages**
Priority: P0, required pre-launch (blocks full revenue activation)
Work: Add `cta-button--pending` + `data-affiliate-status="pending"` to all condition/insurance platform card CTAs; update activate-affiliate.py to target all page types by platform slug

**PS-CSS-CLEANUP-01 — Delete stale root styles.css, run duplicate CSS audit**
Priority: P1
Work: Delete/rename `templates/styles.css` at repo root; run `assets/find_all_dupes.py`; document and resolve top cascade conflicts before PS-DESIGN-01

**PS-CEREBRAL-REVIEW — Full editorial review of cerebral-review.html**
Priority: P1, required pre-launch
Risk: DEA/regulatory history disclosure may affect affiliate relationship; confirm accuracy, tone, and proportionality

**PS-AFFILIATE-OUTREACH-01 — Submit first affiliate applications**
Priority: P0, on critical path for launch revenue
Programs: Online-Therapy.com direct → Calmerry direct → Talkspace (CJ) → BetterHelp (Impact Radius)
Timeline: Apply now — 2–4 week approval window; this is blocking revenue at launch


---

## Launch Readiness Checklist

### Hard Blockers — do not launch without these

- [ ] Domain repurchase — Gavin (no timeline in STATUS.md)
- [ ] Editorial reviewer decision — resolve whether Dr. Sarah Chen is a real contracted LCSW, a fictional persona with explicit disclosure, or other; update editorial policy accordingly
- [ ] Affiliate applications submitted — apply to at least 3 programs now; approval is on critical path (2–4 weeks)
- [ ] NOCD blank pricing fields — FIX-3 (P0 content bug, visibly broken on live page)
- [ ] Condition/insurance CTA pending pattern — 51 pages + activate-affiliate.py update (PS-AFFILIATE-CTA-FIX-01)
- [ ] Reviewer bio link — fix or remove "View full bio →" on all 97 pages (currently href="#")
- [ ] FTC inline affiliate disclosure near CTA buttons — FIX-6 (required before any affiliate links go live)

### Recommended Pre-Launch — high value, low effort

- [ ] `--clr-primary` broken variable fix — FIX-1
- [ ] ADHD Online wrong href in reviews.html — FIX-2
- [ ] Duplicate favicon tags in insurance/condition pages — FIX-4
- [ ] Footer Quick Links: add Conditions entry across non-hub pages — FIX-5
- [ ] Full read of cerebral-review.html for regulatory disclosure accuracy
- [ ] 10 priority review pages content enrichment — PS-CONTENT-ENRICH-01
- [ ] Fraunces font: wire to use case or remove from import — Finding 1.1

### Post-Launch

- [ ] Google Search Console property creation and sitemap.xml submission
- [ ] First crawl monitoring — watch for unexpected 404s
- [ ] datePublished in Review JSON-LD updated to actual publication dates
- [ ] Logo refresh when solid-background assets sourced (PS-LOGO-REFRESH-01 — backlogged, blocked on assets)
- [ ] CSS duplicate audit and cleanup — PS-CSS-CLEANUP-01

### Completed ✅

- [x] 97 pages built and live on Vercel
- [x] Clean URL routing confirmed (/reviews, /conditions, /insurance, /betterhelp-review, etc.)
- [x] sitemap.xml at /sitemap.xml and robots.txt at /robots.txt
- [x] Canonicals on all 97 pages
- [x] BreadcrumbList JSON-LD on all 97 pages
- [x] FAQPage JSON-LD on all condition + insurance pages
- [x] Review JSON-LD on all 34 review pages
- [x] data-affiliate-status="pending" + cta-button--pending on all 34 review page CTAs
- [x] activate-affiliate.py documented and ready for review pages
- [x] 404 page styled and live
- [x] Crisis resources footer on every page
- [x] SEO meta descriptions 120–160 chars, all 97 pages
- [x] No emoji anywhere — icon ban holding
- [x] Inline affiliate disclosure section at bottom of all review pages
- [x] Footer Quick Links pointing to hub pages (Conditions entry missing from non-hub pages — see FIX-5)
