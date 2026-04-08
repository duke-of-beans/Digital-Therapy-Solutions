# Digital Therapy Solutions — STATUS.md
Last Updated: 2026-04-08 (polish pass — FIX-1 through FIX-6 complete)

## Sprints

| Sprint | Name | Status | Commit |
|---|---|---|---|
| PS-PROP-01 | Initial build — 21 pages | ✅ COMPLETE | (initial) |
| PS-PROP-01-FIX | Nav/CSS unification — 9 pages fixed | ✅ COMPLETE | 590a427 |
| PS-HUB-01 | Hub pages + nav update + breadcrumbs | ✅ COMPLETE | e4a7211 |
| PS-CONDITIONS-01 | 20 condition pages + conditions.html fully live (24 cards) | ✅ COMPLETE | 889f7dc |
| PS-INSURANCE-01 | 17 insurer logos + 17 stub pages + insurance.html all live | ✅ COMPLETE | b90b345 |
| PS-DESIGN-QA-01 | Design quality pass — icons, logos, typography, layout variants | ✅ COMPLETE | 682bb37 |
| PS-CONDITIONS-02 | 4 remaining condition pages — conditions vertical 28/28 | ✅ COMPLETE | 16ad1e8 |
| PS-SEO-01 | Canonicals, structured data, sitemap, robots, meta audit | ✅ COMPLETE | 1094e09 |
| PS-DESIGN-QA-02 | Vercel routing, footer links, logos, layout variety | ✅ COMPLETE | 27a767d |
| PS-ROUTING-FIX | vercel.json outputDirectory — clean URLs confirmed live | ✅ COMPLETE | db10564 |
| PS-PLATFORMS-01 | 31 review pages + affiliate toggle system | ✅ COMPLETE | 463301e |
| PS-AUDIT-01 | Full multi-hat site audit — Designer/Engineer/Owner/Affiliate | ✅ COMPLETE | — |
| PS-DESIGN-01 | MORPH-26 design intelligence pass | ⬜ QUEUED | — |
| PS-AFFILIATE-CTA-FIX-01 | CTA direct links + CSS fix — 93 CTAs live, 0 dead | ✅ COMPLETE | — |
| PS-IMAGE-01 | Unsplash image enhancement — hero differentiation + emotional rhythm injection | 🔄 IN PROGRESS | 1fe83dd |


## PS-AUDIT-01 Notes
- Full multi-hat audit complete — 9 pages read in full, targeted spot-checks across all 5 verticals
- Report: PS-AUDIT-01-REPORT.md
- P0 findings: NOCD blank pricing (nocd-review.html), condition/insurance CTAs not using pending pattern (51 pages), activate-affiliate.py only covers review pages
- P1 findings: `--clr-primary` broken variable (renders blue not teal), ADHD Online wrong href in reviews.html, footer missing Conditions link on non-hub pages, FTC inline disclosure gap, reviewer bio link dead on all 97 pages, 31 new review pages are thin vs flagship depth
- New backlog items added: PS-AFFILIATE-CTA-FIX-01 (P0), PS-CONTENT-ENRICH-01 (P1), PS-REVIEWER-BIO-01 (P1), PS-CSS-CLEANUP-01 (P1), PS-AFFILIATE-OUTREACH-01 (P0), PS-CEREBRAL-REVIEW (P1)
- Launch readiness: NOT YET — domain (Gavin), reviewer persona decision, affiliate applications are hard external blockers
- FIX NOW queue: 6 items, all executable in <3 tool calls each — see report

## PS-PLATFORMS-01 Notes
- 31 new review pages built — all follow betterhelp-review.html structure
- All 34 review pages (including 3 existing) use data-affiliate-status="pending" pending CTA pattern
- assets/activate-affiliate.py ready: py assets/activate-affiliate.py --platform [slug] --url [url]
- .cta-button--pending CSS added to templates/styles.css
- reviews.html: all 34 cards live-linked, 0 stubs
- output/sitemap.xml regenerated: 97 URLs
- Quality gate: 0 failures, 97 pages

## PS-DESIGN-QA-02 Notes
- vercel.json at repo root — clean URLs live (/reviews, /betterhelp-review, etc.)
- output/404.html — styled 404 page added
- Footer links patched on 62 pages — Quick Links now → reviews.html + insurance.html
- Platform logo Clearbit regrab: 0/34 PASS (DNS blocked on host — backlogged)
- .hub-card__logo img: object-fit: contain fixed in styles.css
- privacy-policy.html: attorney disclaimer removed
- how-online-therapy-works.html: fully restyled (hero, timeline, split-section, stat-callouts)
- Layout variety applied to 6 detail pages (betterhelp, talkspace, online-therapy-com, aetna, bcbs, cigna)
- Quality gate: 0 failures, 66 pages

## PS-SEO-01 Notes
- Meta descriptions: 65/65 at 120-160 chars (23 were flagged, all fixed)
- Canonicals: 65/65 pages
- BreadcrumbList JSON-LD: 65/65 pages
- FAQPage JSON-LD: 28 condition + 23 insurance pages
- Review JSON-LD: BetterHelp (4.5★), Talkspace (4.3★), Online-Therapy.com (4.1★)
- sitemap.xml: 65 URLs, priority tiers, valid XML
- robots.txt: Allow: /, Sitemap directive
- Internal links: 65/65 pages ≥3 body links (4 pages patched: privacy-policy, about, affiliate-disclosure, editorial-policy)
- Quality gate: 0 failures

## Open Items
- ✅ P0: ~~nocd-review.html — blank pricing placeholders~~ → DONE: $280/mo stat callout, $20-40 copay / $260-300/mo self-pay copy (2026-04-08)
- ✅ P0: ~~51 condition/insurance pages — CTAs need pending pattern~~ → DONE: 93 direct CTAs live (PS-AFFILIATE-CTA-FIX-01)
- P0: Affiliate applications — apply to all 32 programs with affiliate programs (assets/platform-registry.json); activate with: py assets/activate-affiliate.py --platform [slug] --url [url]
- ✅ P0: ~~--clr-primary broken CSS variable~~ → DONE: confirmed clean across all 97 pages
- ✅ P1: ~~ADHD Online wrong href in reviews.html~~ → DONE: fixed to adhd-online-review.html (2026-04-08)
- ✅ P1: ~~Footer Quick Links missing Conditions entry on non-hub pages~~ → DONE: added to 94 pages (2026-04-08)
- ✅ P1: ~~FTC inline disclosure missing near CTA buttons~~ → DONE: 126 insertions across 65 pages (2026-04-08)
- ✅ P1: ~~Reviewer bio "View full bio" links to href="#"~~ → DONE: all 34 review pages → editorial-policy.html#editorial-team (2026-04-08)
- ✅ P2: ~~Fraunces dead font load~~ → DONE: removed from all 97 pages (2026-04-08)
- ✅ P2: ~~Duplicate favicon tags on condition/insurance pages~~ → DONE: 52 tags removed from 26 pages (2026-04-08)
- ✅ P1: ~~PS-CONTENT-ENRICH-01~~ → DONE: Our Relationship, Cerebral, NOCD all enriched to flagship depth (2026-04-08). All 10 priority review pages complete.
- Next: PS-DESIGN-01 (MORPH-26 design intelligence pass)

## PS-CSKY Session Improvements (2026-04-03) — Principles to apply
The following design and UX improvements were established in the Clear Sky Travel Planning
build and must be applied to DTS before launch. Each is a named principle with spec docs.

- [ ] **PS-DTS-ICON-01** — Icon system audit: replace any emoji with inline SVG. Apply
  two-color token system: `--color-icon` (lighter, brand mark) vs `--color-sky` (interactive).
  All icon containers use `background: var(--color-icon-light)`. Spec: DESIGN_SYSTEM_SPEC.md

- [ ] **PS-DTS-WCAG-01** — WCAG photo surface pass: any white text over images needs
  text-shadow, strengthened gradient overlays (min 0.88 at bottom), and dark glass tags
  (NOT white glass). Critical for healthcare site accessibility. Spec: DESIGN_SYSTEM_SPEC.md §5

- [ ] **PS-DTS-RHYTHM-01** — Emotional rhythm image injection audit: DTS copy is deeply
  emotional (people in distress seeking help). Every section that evokes relief, hope, or
  trust needs visual follow-through within 2-3 scrolls. Run image rhythm audit per
  IMAGE_INJECTION_STRATEGY.md emotional rhythm rule.

- [ ] **PS-DTS-BUTTON-01** — Button shape consistency: all primary CTAs use pill shape
  (border-radius: 100px). Secondary/functional buttons use soft corner (8px). No exceptions.

- [ ] **PS-DTS-FONT-01** — Typography warmth: any data values shown to users (prices, session
  counts, platform ratings) must use Inter/primary font, NOT monospace. Mono is tabular data
  only. Spec: DESIGN_SYSTEM_SPEC.md §2.2

- [ ] **PS-DTS-REINFORCE-01** — Decision reinforcement system: picking a therapy platform is
  anxiety-inducing. Add specific, data-backed validation copy after each major decision point
  (platform chosen, insurance verified, appointment booked). This is the highest-value UX
  addition for a healthcare affiliate site. Spec: UX_PATTERNS.md §2

- [ ] **PS-DTS-ANIM-01** — Smart animations: JS parallax on full-bleed image breaks, stat
  value spring animation on scroll-in, staggered card reveals in grids, hero entrance stagger.
  Spec pattern: PS-CSKY-12 implementation in Clear Sky japan.html.

- [ ] **PS-DTS-EQUITABLE-01** — Equitable visuals audit: every component, widget, or data
  point added going forward needs visual representation from day one. Image slots required
  in all section templates. Spec: DESIGN_SYSTEM_SPEC.md §8

## Known Technical Patterns
- Python inline commands via cmd fail at ~500+ chars — always write to file first
- sys.stdout.reconfigure(encoding='utf-8') is correct UTF-8 fix; PYTHONUTF8=1 via set does not persist
- git commit -m with parens/dashes gets tokenized wrong by Desktop Commander — always use commit-msg.txt + git commit -F
- Emoji permanently banned — all icons must be cohesive inline SVG, stroke-based (see icons-ban.md)
- Clearbit logo.clearbit.com blocked by DNS on host — use browser save or alternative source
- CSS CRITICAL: templates/styles.css and output/templates/styles.css are DIVERGED. Always edit output/templates/styles.css directly. Never copy from templates/styles.css — it will overwrite with stale rules. Use Desktop Commander:edit_block on output/templates/styles.css only.
- CSS CRITICAL: Multiple duplicate CSS rules in output/templates/styles.css from sprint history — run assets/find_dupes.py before adding new rules to check for conflicts.
- CSS BUG: `--clr-primary` is used in inline styles across multiple HTML files but NOT defined in :root. Correct variable is `--accent-primary`. Affects link colors on review and condition pages (renders as browser default blue). Fix via bulk replace before launch.
- AFFILIATE BUG: activate-affiliate.py only targets data-affiliate-status="pending" on review pages. Condition/insurance pages use bare href="#" CTAs — they will NOT activate when affiliate contracts are signed. Fix: add pending pattern to 51 pages + update script.

## Page Inventory

### Reviews (34 live / 34 total) ✅ COMPLETE
- [x] betterhelp-review.html, talkspace-review.html, online-therapy-com-review.html
- [x] adhd-online-review.html, amwell-review.html, bend-health-review.html, brightline-review.html, brightside-review.html, calmerry-review.html, cerebral-review.html, circle-medical-review.html, doctor-on-demand-review.html, done-adhd-review.html
- [x] faithful-counseling-review.html, gay-therapy-center-review.html, grow-therapy-review.html, headspace-review.html, headway-review.html, inclusive-therapists-review.html, klarity-review.html, lunajoy-review.html, manatee-health-review.html, mindful-care-review.html
- [x] nocd-review.html, open-path-review.html, our-relationship-review.html, our-ritual-review.html, pride-counseling-review.html, psychology-today-review.html, regain-review.html, simplepractice-review.html, talkiatry-review.html, teen-counseling-review.html, therapyden-review.html

### Conditions (28 live / 28 total) ✅ COMPLETE
- [x] anxiety.html, depression.html, adhd.html, couples.html
- [x] ocd.html, ptsd.html, bipolar.html, eating-disorders.html
- [x] grief.html, anger.html, addiction.html, stress.html, burnout.html
- [x] relationship.html, lgbtq.html, teen.html, postpartum.html
- [x] insomnia.html, chronic-pain.html, social-anxiety.html
- [x] phobias.html, panic.html, loneliness.html, self-esteem.html
- [x] mens-mental-health.html, womens-mental-health.html
- [x] life-transitions.html, autism.html

### Insurance (23 live / 23 total) ✅ COMPLETE
- [x] aetna.html, bcbs.html, cigna.html, unitedhealthcare.html, medicaid.html, affordable.html
- [x] humana.html, kaiser.html, anthem.html, molina.html, oscar.html, ambetter.html
- [x] wellcare.html, tricare.html, chip.html, medicare.html, beacon.html
- [x] magellan.html, centene.html, highmark.html, harvard-pilgrim.html, tufts.html, community-health.html

### Hub Pages (3 live / 3 total) ✅ COMPLETE
- [x] reviews.html, conditions.html, insurance.html

### Supporting Pages (8 live)
- [x] index.html, about.html, editorial-policy.html, affiliate-disclosure.html
- [x] privacy-policy.html, crisis-resources.html, how-online-therapy-works.html, do-i-need-therapy.html

### SEO Files
- [x] output/sitemap.xml ✅
- [x] output/robots.txt ✅

## Launch Blockers
- [x] Domain — ✅ purchased and live (digitaltherapysolutions.com)
- [x] Editorial reviewer — ✅ DTS Research Team branding (Dr./LCSW/Licensed credentials scrubbed 2026-04-08)
- [x] Hero images — ✅ fixed 2026-04-08 (were missing from output/assets/)
- [ ] Affiliate applications — in progress (see below)

## Affiliate Application Status (as of 2026-04-08)
Registry: assets/platform-registry.json — 32 programs with affiliate programs (SimplePractice + Psychology Today excluded)
Tracker: assets/activate-affiliate.py --status (run to see live vs direct CTA counts)
Activate: py assets/activate-affiliate.py --platform [slug] --url [affiliate-url]

### Network Verification
- [x] Impact Radius — ✅ meta tag verified (index.html head)
- [ ] FlexOffers — verification submitted (meta tag + fo-verify.html in output root), pending confirmation
- [ ] Commission Junction — not yet started

### Applications In Progress
Priority 1 (direct programs, no traffic minimum):
- Online-Therapy.com, Calmerry, Grow Therapy, Headway, Brightside, NOCD, Talkiatry,
  Klarity, Open Path Collective, Inclusive Therapists, ADHD Online, Circle Medical,
  Done, Lunajoy, Our Ritual, OurRelationship, TherapyDen, Gay Therapy Center

Priority 2 (network programs, may require traffic verification):
- BetterHelp (Impact Radius), Talkspace (CJ), ReGain (IR), Teen Counseling (IR),
  Pride Counseling (IR), Faithful Counseling (IR), Cerebral (direct),
  Amwell (CJ), Headspace (IR), Doctor on Demand (CJ),
  Brightline, Bend Health, Manatee, Mindful Care

### W-9 Notes
- Entity: Borrowed Light Group LLC
- Box 2: Borrowed Light Group LLC | Box 3: LLC → D (disregarded) | Part I: BLG EIN
- E-sign acceptable, no wet ink required
