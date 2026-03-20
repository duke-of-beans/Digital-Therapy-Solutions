# Digital Therapy Solutions — STATUS.md
Last Updated: 2026-03-20

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
| PS-PLATFORMS-01 | 31 review pages + affiliate toggle system | ✅ COMPLETE | TBD |
| PS-DESIGN-01 | MORPH-26 design intelligence pass | ⬜ QUEUED | — |


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
- None. Next: PS-DESIGN-01 (MORPH-26 design intelligence pass)

## Known Technical Patterns
- Python inline commands via cmd fail at ~500+ chars — always write to file first
- sys.stdout.reconfigure(encoding='utf-8') is correct UTF-8 fix; PYTHONUTF8=1 via set does not persist
- git commit -m with parens/dashes gets tokenized wrong by Desktop Commander — always use commit-msg.txt + git commit -F
- Emoji permanently banned — all icons must be cohesive inline SVG, stroke-based (see icons-ban.md)
- Clearbit logo.clearbit.com blocked by DNS on host — use browser save or alternative source

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
