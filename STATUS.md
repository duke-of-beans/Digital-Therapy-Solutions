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
| PS-PLATFORMS-01 | 31 remaining platform review pages | ⬜ QUEUED (blocked: affiliate apps) | — |
| PS-DESIGN-01 | MORPH-26 design intelligence pass | ⬜ QUEUED | — |

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
- None.

## Known Technical Patterns
- Python inline commands via cmd fail at ~500+ chars — always write to file first
- sys.stdout.reconfigure(encoding='utf-8') is correct UTF-8 fix; PYTHONUTF8=1 via set does not persist
- git commit -m with parens/dashes gets tokenized wrong by Desktop Commander — always use commit-msg.txt + git commit -F
- Emoji permanently banned — all icons must be cohesive inline SVG, stroke-based (see icons-ban.md)
- Clearbit logo.clearbit.com blocked by DNS on host — use browser save or alternative source

## Page Inventory

### Reviews (3 live / 34 total)
- [x] betterhelp-review.html, talkspace-review.html, online-therapy-com-review.html
- [ ] 31 pages — see PS-PLATFORMS-01

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
