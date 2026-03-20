# Digital Therapy Solutions — STATUS.md
Last Updated: 2026-03-20 (PS-AUDIT-01)

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
- P0: nocd-review.html — blank pricing placeholders (see FIX-3 in PS-AUDIT-01-REPORT.md)
- P0: 51 condition/insurance pages — CTAs need pending pattern (PS-AFFILIATE-CTA-FIX-01)
- P0: Affiliate applications — submit to Online-Therapy.com + Calmerry immediately (PS-AFFILIATE-OUTREACH-01)
- P1: `--clr-primary` broken CSS variable across multiple pages (FIX-1)
- P1: ADHD Online wrong href in reviews.html (FIX-2)
- P1: Footer Quick Links missing Conditions entry on non-hub pages (FIX-5)
- P1: FTC inline disclosure missing near CTA buttons (FIX-6)
- P1: Reviewer bio "View full bio" links to href="#" on all 97 pages (PS-REVIEWER-BIO-01)
- P1: 31 new review pages thin vs flagship — needs content enrichment (PS-CONTENT-ENRICH-01)
- Next code sprint: PS-DESIGN-01 (MORPH-26) — hold until FIX NOW queue is resolved

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
- [ ] Domain repurchase (Gavin)
- [ ] Editorial reviewer onboarded
- [ ] Affiliate applications submitted + accepted
- [x] inclusive-therapists.webp ✅ converted and committed
- [x] All content sprints complete ✅
- [x] SEO hardening complete ✅
