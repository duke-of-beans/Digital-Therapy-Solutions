# DTS — MORNING BRIEFING
Date: 2026-04-08
Project: Digital Therapy Solutions (Proper Sluice Property #1)
Repo: duke-of-beans/Digital-Therapy-Solutions
Live: https://digitaltherapysolutions.com
Last commit: 889ab00 (FlexOffers verification)

---

## Session Summary

Long affiliate sprint. Site went from broken/unready to genuinely application-ready.

### What shipped today (4 commits)

| Commit | What |
|--------|------|
| 64d1b3c | PS-AFFILIATE-CTA-FIX-01 — 93 dead CTAs replaced with direct links across 31 condition/insurance pages. activate-affiliate.py rebuilt site-wide. platform-registry.json created (32 programs). --clr-primary CSS bug fixed all 97 pages. |
| 69308aa | Hero images fixed — 7 images missing from output/assets/ (hero-home, hero-emotional, hero-couples, hero-focus, hero-practical, hero-review, forks-reading). All heroes now load. |
| 51de217 | False credential scrub — Dr. prefix, LCSW, Licensed Clinical Social Worker removed from 5 pages (adhd, cigna, couples, depression, do-i-need-therapy). SC initials → DTS on 2 pages. |
| d88234e | Impact Radius site verification meta tag added to index.html head. |
| 889ab00 | FlexOffers verification — fo-verify.html added to output root + meta tag in index.html. |

---

## Affiliate Application Status

**Networks verified:**
- Impact Radius ✅ (meta tag live)
- FlexOffers — pending (meta tag + HTML file submitted, awaiting confirmation)
- Commission Junction — not started

**Programs:** 32 total eligible
- Priority 1 (direct, no traffic minimum): 18 programs
- Priority 2 (network, may require traffic): 14 programs

**Application answers (use for every program):**
1. Site: https://www.digitaltherapysolutions.com — 97-page independent editorial review site covering platforms, conditions, insurance
2. Traffic: Early organic indexing, projecting 500–2,000/mo within 90 days as pages index. Content-first model.
3. Purpose: Independent editorial resource. "We don't generate curiosity clicks, we generate decided buyers."

**W-9 ready:**
- BLG EIN active
- Box 3: LLC → D (disregarded entity)
- E-sign acceptable

**To activate an approved affiliate:**
```
py assets\activate-affiliate.py --platform [slug] --url [your-affiliate-url]
py assets\activate-affiliate.py --status   # see live vs direct counts
py assets\activate-affiliate.py --list     # see all 32 programs
```

---

## Open Items

**P0 — do next:**
- [ ] Continue affiliate applications across 32 programs (tracker in assets/platform-registry.json)
- [ ] Confirm FlexOffers verification passed
- [ ] Start Commission Junction registration
- [ ] nocd-review.html — blank pricing placeholders still unfilled

**P1 — before meaningful traffic:**
- [ ] PS-CONTENT-ENRICH-01 — 10 thin review pages need flagship depth
- [ ] PS-DTS-* improvements from Clear Sky session (WCAG, icons, rhythm, buttons, fonts, animations)
- [ ] ADHD Online wrong href in reviews.html (links to betterhelp-review)
- [ ] Footer Quick Links missing Conditions on non-hub pages
- [ ] FTC inline disclosure missing adjacent to CTA buttons
- [ ] Reviewer bio "View full bio" links to href=# on all 97 pages

**Future:**
- [ ] PS-DESIGN-01 (MORPH-26 design intelligence pass) — queued
- [ ] GSC setup for traffic visibility once indexing begins
- [ ] datePublished JSON-LD bulk update (all pages hardcoded 2026-01-01)

---

## Key Files
- Registry: D:\Work\Digital-Therapy-Solutions\assets\platform-registry.json
- Activate script: D:\Work\Digital-Therapy-Solutions\assets\activate-affiliate.py
- Patch script: D:\Work\Digital-Therapy-Solutions\assets\patch-cta-direct.py
- Verification section: output/index.html <head> — labeled block for future network tags
- Vercel project: davids-projects-b0509900 (Hobby, deploy via git push only)
- CSS canonical: output/templates/styles.css ONLY (root templates/styles.css is stale)
- New images must go to output/assets/ NOT root assets/
