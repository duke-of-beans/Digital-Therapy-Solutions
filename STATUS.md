# Digital Therapy Solutions — STATUS.md
Last Updated: 2026-03-19

## Sprints

| Sprint | Name | Status | Commit |
|---|---|---|---|
| PS-PROP-01 | Initial build — 21 pages | ✅ COMPLETE | (initial) |
| PS-PROP-01-FIX | Nav/CSS unification — 9 pages fixed | ✅ COMPLETE | 590a427 |
| PS-HUB-01 | Hub pages + nav update + breadcrumbs | ✅ COMPLETE | e4a7211 |
| PS-CONDITIONS-01 | 20 condition pages + conditions.html fully live (24 cards) | ✅ COMPLETE | 889f7dc |
| PS-INSURANCE-01 | Logo grab + 17 stub insurer pages | ✅ COMPLETE | TBD |
| PS-PLATFORMS-01 | 31 remaining platform review pages | ⬜ QUEUED (blocked: affiliate apps) | — |
| PS-SEO-01 | Meta, schema, sitemap, internal links | ⬜ QUEUED | — |
| PS-DESIGN-01 | MORPH-26 design intelligence pass | ⬜ QUEUED | — |

## PS-INSURANCE-01 Notes
- 17/17 insurer logos grabbed successfully (all WebP, assets/logos/insurer-*.webp)
- 17 stub pages built with substantive content — coverage status, platforms, copay range, how-to-check steps
- insurance.html updated: all 23 cards live-linked, all with logo img + onerror fallback
- 6 original live insurer logos (aetna, bcbs, cigna, uhc, medicaid) not yet grabbed — onerror fallback to initials active, visual parity maintained
- build-insurer-pages.py generator script retained in assets/ for future updates

## PS-CONDITIONS-01 Notes
- conditions.html finalized with 28 total entries: 24 live + 4 stubs (Men's Mental Health,
  Women's Mental Health, Life Transitions, Autism & Neurodivergence)
- "Stress & Burnout" split into separate stress.html + burnout.html — confirm split is intentional
- Men's/Women's/Life Transitions/Autism slugs to be confirmed and added to PS-CONTENT-02 or PS-CONDITIONS-02

## Known Technical Patterns (established this project)
- Python inline commands via cmd fail at ~500+ chars (Windows arg length limit) — always write to file first
- sys.stdout.reconfigure(encoding='utf-8') is correct UTF-8 fix; PYTHONUTF8=1 via set does not persist
- Desktop Commander read_file returns metadata only for .md files — use cmd type as fallback

## Page Inventory

### Reviews (3 live / 34 total)
- [x] betterhelp-review.html
- [x] talkspace-review.html
- [x] online-therapy-com-review.html
- [ ] 31 pages — see PS-PLATFORMS-01

### Conditions (24 live + 4 stubs / 28 total)
- [x] anxiety.html
- [x] depression.html
- [x] adhd.html
- [x] couples.html
- [x] ocd.html
- [x] ptsd.html
- [x] bipolar.html
- [x] eating-disorders.html
- [x] grief.html
- [x] anger.html
- [x] addiction.html
- [x] stress.html
- [x] burnout.html
- [x] relationship.html
- [x] lgbtq.html
- [x] teen.html
- [x] postpartum.html
- [x] insomnia.html
- [x] chronic-pain.html
- [x] social-anxiety.html
- [x] phobias.html
- [x] panic.html
- [x] loneliness.html
- [x] self-esteem.html
- [ ] mens-mental-health.html (stub on hub — slug TBD)
- [ ] womens-mental-health.html (stub on hub — slug TBD)
- [ ] life-transitions.html (stub on hub — slug TBD)
- [ ] autism.html (stub on hub — slug TBD)

### Insurance (23 live / 23 total) ✅
- [x] aetna.html
- [x] bcbs.html
- [x] cigna.html
- [x] unitedhealthcare.html
- [x] medicaid.html
- [x] affordable.html
- [x] humana.html
- [x] kaiser.html
- [x] anthem.html
- [x] molina.html
- [x] oscar.html
- [x] ambetter.html
- [x] wellcare.html
- [x] tricare.html
- [x] chip.html
- [x] medicare.html
- [x] beacon.html
- [x] magellan.html
- [x] centene.html
- [x] highmark.html
- [x] harvard-pilgrim.html
- [x] tufts.html
- [x] community-health.html

### Hub Pages (3 live / 3 total)
- [x] reviews.html
- [x] conditions.html
- [x] insurance.html

### Supporting Pages (8 live)
- [x] index.html
- [x] about.html
- [x] editorial-policy.html
- [x] affiliate-disclosure.html
- [x] privacy-policy.html
- [x] crisis-resources.html
- [x] how-online-therapy-works.html
- [x] do-i-need-therapy.html

## Launch Blockers
- [ ] Domain repurchase (Gavin)
- [ ] Editorial reviewer onboarded
- [ ] Affiliate applications submitted + accepted
- [x] PS-HUB-01 complete ✅
- [x] PS-CONDITIONS-01 complete ✅
- [x] PS-INSURANCE-01 complete ✅

## Assets
- Platform logos: 34 WebPs in assets/logos/ ✅
- Insurance logos: 17 new insurer logos ✅ (insurer-*.webp) | 6 original live insurer logos not yet grabbed (fallback active)
- Hero images: 3 WebPs ✅
- Branding: favicon, logo-icon, logo-wordmark ✅
