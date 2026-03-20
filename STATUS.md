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
| PS-SEO-01 | Meta, schema, sitemap, robots, internal links | ✅ COMPLETE | 1094e09 |
| PS-PLATFORMS-01 | 31 remaining platform review pages | ⬜ QUEUED (blocked: affiliate apps) | — |
| PS-DESIGN-01 | MORPH-26 design intelligence pass | ⬜ QUEUED | — |

## PS-SEO-01 Notes
- Meta descriptions: all 65 pages at 120–160 chars (23 fixed from LONG/SHORT)
- Canonicals: all 65 pages — `<link rel="canonical">` in `<head>`
- BreadcrumbList JSON-LD: all 65 pages
- FAQPage JSON-LD: 28 condition pages + 23 insurance pages (51 total)
- Review JSON-LD: betterhelp-review.html, talkspace-review.html, online-therapy-com-review.html
- sitemap.xml: output/sitemap.xml ✅ — 65 URLs, priority tiers, valid XML
- robots.txt: output/robots.txt ✅ — Allow: /, Sitemap directive
- Internal links: all 65 pages at ≥3 body content links (4 pages patched: privacy-policy, about, affiliate-disclosure, editorial-policy)
- Quality gate: 65 pages, 0 failures
- Logo grab (inclusive-therapists.webp): BLOCKED — Cowork VM has no outbound DNS. Deferred to PS-DESIGN-01 or manual grab via browser.

## PS-CONDITIONS-02 Notes
- mens-mental-health.html, womens-mental-health.html, life-transitions.html, autism.html — all 3 cards each
- conditions.html — all 28 cards live-linked, hub-card--stub removed, div → a href, SVG icons added
- inclusive-therapists.webp referenced in autism.html but not in original 34-logo set — onerror fallback
  shows initials "IT" until logo added. Flag for next logo regrab or PS-DESIGN-01.
- Quality gate: 65 pages, 0 failures

## Known Technical Patterns
- Python inline commands via cmd fail at ~500+ chars — always write to file first
- sys.stdout.reconfigure(encoding='utf-8') is correct UTF-8 fix; PYTHONUTF8=1 via set does not persist
- git commit -m with parens/dashes gets tokenized wrong by Desktop Commander — always use commit-msg.txt + git commit -F
- Emoji permanently banned — all icons must be cohesive inline SVG, stroke-based (see icons-ban.md)
- `python` not on PATH in Cowork shell — use `py` launcher
- Cowork VM has no outbound DNS — Python `requests` cannot hit external APIs. Pre-fetch assets on host or use Claude in Chrome.
- bs4 (BeautifulSoup) not pre-installed — run `py -m pip install beautifulsoup4 lxml` at sprint start

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

## Launch Blockers
- [ ] Domain repurchase (Gavin)
- [ ] Editorial reviewer onboarded
- [ ] Affiliate applications submitted + accepted
- [ ] inclusive-therapists.webp missing from assets/logos/ (autism.html showing fallback) — grab via browser, not Cowork VM
- [x] All content sprints complete ✅ (conditions 28/28, insurance 23/23, hubs 3/3)
- [x] SEO layer complete ✅ (PS-SEO-01)

## Assets
- Platform logos: 34 WebPs in assets/logos/ (inclusive-therapists.webp missing — needs grab)
- Insurance logos: 17 WebPs in assets/logos/insurer-*.webp ✅
- Hero images: 3 WebPs ✅
- Branding: favicon, logo-icon, logo-wordmark ✅
- sitemap.xml: output/sitemap.xml ✅
- robots.txt: output/robots.txt ✅
