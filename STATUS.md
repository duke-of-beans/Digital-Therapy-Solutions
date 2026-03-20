# Digital Therapy Solutions — STATUS.md
Last Updated: 2026-03-19

## Sprints

| Sprint | Name | Status | Commit |
|---|---|---|---|
| PS-PROP-01 | Initial build — 21 pages | ✅ COMPLETE | (initial) |
| PS-PROP-01-FIX | Nav/CSS unification — 9 pages fixed | ✅ COMPLETE | 590a427 |
| PS-HUB-01 | Hub pages + nav update + breadcrumbs | ✅ COMPLETE | e4a7211 |
| PS-CONDITIONS-01 | 20 condition pages + conditions.html fully live (24 cards) | ✅ COMPLETE | 889f7dc |
| PS-INSURANCE-01 | 17 insurer logos + 17 stub pages + insurance.html all live | ✅ COMPLETE | b90b345 |
| PS-DESIGN-QA-01 | Design quality pass — icons, logos, typography, layout variants | ✅ COMPLETE | 682bb37 |
| PS-CONDITIONS-02 | 4 remaining stub condition pages | ⬜ QUEUED | — |
| PS-PLATFORMS-01 | 31 remaining platform review pages | ⬜ QUEUED (blocked: affiliate apps) | — |
| PS-SEO-01 | Meta, schema, sitemap, internal links | ⬜ QUEUED | — |
| PS-DESIGN-01 | MORPH-26 design intelligence pass | ⬜ QUEUED | — |

## PS-DESIGN-QA-01 Notes
- Emoji permanently banned sitewide — icons-ban.md in repo root as standing policy
- 28 condition tile icons replaced with cohesive stroke SVGs
- legal-hero class applied to privacy-policy.html and affiliate-disclosure.html
- Verdict-box + pull-quote HTML on 6 pages (betterhelp, talkspace, online-therapy-com, aetna, bcbs, cigna)
- Feature-list pros/cons applied to betterhelp and talkspace review pages
- 10 new CSS component classes added to styles.css
- Logo audit: 51 logos scanned, 23 flagged — LOGO_AUDIT.md + assets/regrab-logos.py ready
- MANUAL STEP PENDING: run `python assets/regrab-logos.py` from host to pull 23 flagged logos
  (Clearbit fetch blocked in sandbox, needs host network)

## Known Technical Patterns
- Python inline commands via cmd fail at ~500+ chars — always write to file first
- sys.stdout.reconfigure(encoding='utf-8') is correct UTF-8 fix; PYTHONUTF8=1 via set does not persist
- git commit -m with parens/dashes gets tokenized wrong by Desktop Commander — always use commit-msg.txt + git commit -F
- Emoji permanently banned — all icons must be cohesive inline SVG, stroke-based, humanist style (see icons-ban.md)

## Page Inventory

### Reviews (3 live / 34 total)
- [x] betterhelp-review.html
- [x] talkspace-review.html
- [x] online-therapy-com-review.html
- [ ] 31 pages — see PS-PLATFORMS-01

### Conditions (24 live + 4 stubs / 28 total)
- [x] anxiety.html, depression.html, adhd.html, couples.html
- [x] ocd.html, ptsd.html, bipolar.html, eating-disorders.html
- [x] grief.html, anger.html, addiction.html, stress.html, burnout.html
- [x] relationship.html, lgbtq.html, teen.html, postpartum.html
- [x] insomnia.html, chronic-pain.html, social-anxiety.html
- [x] phobias.html, panic.html, loneliness.html, self-esteem.html
- [ ] mens-mental-health.html (slug confirmed)
- [ ] womens-mental-health.html (slug confirmed)
- [ ] life-transitions.html (slug confirmed)
- [ ] autism.html (slug confirmed)

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
- [ ] Run assets/regrab-logos.py from host (23 flagged logos need Clearbit fetch)
- [x] PS-HUB-01 ✅ | PS-CONDITIONS-01 ✅ | PS-INSURANCE-01 ✅ | PS-DESIGN-QA-01 ✅

## Assets
- Platform logos: 34 WebPs in assets/logos/ (23 flagged for regrab — script ready)
- Insurance logos: 17 WebPs in assets/logos/insurer-*.webp ✅
- Hero images: 3 WebPs ✅
- Branding: favicon, logo-icon, logo-wordmark ✅
