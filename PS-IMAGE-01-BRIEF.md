# PS-IMAGE-01 — Unsplash Image Enhancement Brief
# Digital Therapy Solutions
Last Updated: 2026-04-07

## The Problem

The entire 97-page site runs on 3 reused photos:
- `hero.webp` — used as hero on every single page (85+ pages, same image)
- `video-call-shoulder.webp` — used as visual break on every page that has one
- `video-call-earbuds.webp` — used in the forks split section on index + all condition pages

No body images exist on any condition page, review page, or insurance page.
This is the PS-DTS-RHYTHM-01 gap: a healthcare affiliate site where someone in
distress is deciding whether to get therapy, and visual emotional support is nearly absent.

---

## Delivery Protocol

1. David searches Unsplash with the provided query
2. David downloads the best match and drops it in the specified `assets/` path
3. Claude receives confirmation, writes the inject script or edits directly

All images should be downloaded at max resolution and converted to .webp before drop.
Naming convention: use the exact filename specified below.

---

## TIER 1 — Hero Differentiation (Highest Priority)

Current state: same `hero.webp` on every page. Each category needs its own.

### 1A. Homepage Hero (replace hero.webp)
**Target file:** `assets/hero-home.webp`
**Unsplash query:** `woman couch laptop morning light warm`
**What to look for:** Soft, warm, natural light. Person relaxed, not posed. Feels like a real living room, not a stock set. No clinical imagery.
**Alt text:** "Woman on couch with laptop — researching online therapy from home"

### 1B. Anxiety / Depression / PTSD / OCD Hero
**Target file:** `assets/hero-emotional.webp`
**Unsplash query:** `person window light thoughtful quiet morning`
**What to look for:** Someone near a window, soft directional light, contemplative but not distressed. No tears, no hands-on-head. Introspective, not dramatic.
**Alt text:** "Person by window — quiet moment of reflection"
**Pages:** anxiety.html, depression.html, ptsd.html, ocd.html, grief.html, loneliness.html, self-esteem.html

### 1C. ADHD / Burnout / Focus Hero
**Target file:** `assets/hero-focus.webp`
**Unsplash query:** `person desk working focus minimal clean light`
**What to look for:** Clean environment, person at work or studying, slight sense of motion or energy. Not chaotic, not clinical.
**Alt text:** "Person at desk — focused work environment"
**Pages:** adhd.html, burnout.html, stress.html

### 1D. Couples / Relationship Hero
**Target file:** `assets/hero-couples.webp`
**Unsplash query:** `couple talking coffee kitchen warm candid`
**What to look for:** Two people, relaxed conversation, warm tones. Candid over posed. Not romantic-stock, not clinical.
**Alt text:** "Two people in relaxed conversation at home"
**Pages:** couples.html, relationship.html, our-relationship-review.html, our-ritual-review.html

### 1E. Teens / Youth Hero
**Target file:** `assets/hero-teen.webp`
**Unsplash query:** `teenager bedroom phone natural light authentic`
**What to look for:** Younger person, authentic setting, not a stock smile. Real bedroom or real space.
**Alt text:** "Young person with phone — accessible support from home"
**Pages:** teen.html, teen-counseling-review.html, manatee-health-review.html

### 1F. Review Pages Hero (generic research feel)
**Target file:** `assets/hero-review.webp`
**Unsplash query:** `person reading research notes desk calm`
**What to look for:** Someone reading or researching, thoughtful, calm. Not looking at camera. Conveys "someone did the work for you."
**Alt text:** "Person reviewing notes and research — finding the right platform"
**Pages:** All 34 review pages (betterhelp-review.html etc.)

### 1G. Insurance / Practical Pages Hero
**Target file:** `assets/hero-practical.webp`
**Unsplash query:** `person phone call home relaxed natural light`
**What to look for:** Someone on a phone or laptop in a practical, real-home context. Feels like dealing with something manageable, not stressful.
**Alt text:** "Person at home handling healthcare decisions"
**Pages:** All 23 insurance pages, affordable.html

---

## TIER 2 — Visual Break Variants (Medium Priority)

Current state: `video-call-shoulder.webp` used as full-bleed visual break on every page.

### 2A. Primary visual break variant (replace/supplement video-call-shoulder.webp)
**Target file:** `assets/vb-couch-light.webp`
**Unsplash query:** `couch living room soft light empty peaceful`
**What to look for:** A cozy, calm living space. Can be empty or have a person. Cinematic crop potential (wide, landscape). Warm tones.
**Usage:** Homepage, review pages

### 2B. Secondary visual break
**Target file:** `assets/vb-window-plant.webp`
**Unsplash query:** `window sunlight plant interior calm minimal`
**What to look for:** Interior space with natural light through a window. Plants optional. Calming, hopeful feel.
**Usage:** Condition pages

### 2C. Outdoor/nature break (optional, high impact)
**Target file:** `assets/vb-nature-path.webp`
**Unsplash query:** `path woods morning light peaceful walking`
**What to look for:** A path through trees or open space, soft morning light. The "light at the end of the tunnel" visual without being cliché.
**Usage:** Grief, loneliness, life-transitions pages

---

## TIER 3 — In-Page Emotional Rhythm Injection (High Impact, More Work)

These go INSIDE pages, in the body — not hero, not visual break.
Currently zero in-page photos exist on any condition or review page.

Each image is placed in a `<div class="inline-image">` block between two content sections.
Claude handles the inject once images are delivered.

### 3A. Therapy session / connection image
**Target file:** `assets/inline-session.webp`
**Unsplash query:** `two people talking listening warmth connection`
**What to look for:** Sense of being heard. Two people in conversation. Can be indirect — a hand, leaning in, eye contact. Not clinical.
**Inject on:** betterhelp-review.html, talkspace-review.html, online-therapy-com-review.html, anxiety.html, depression.html

### 3B. Relief / after moment image
**Target file:** `assets/inline-relief.webp`
**Unsplash query:** `person deep breath eyes closed sunlight relief calm`
**What to look for:** Someone mid-exhale, eyes closed, sun on face. The "weight off my shoulders" visual.
**Inject on:** anxiety.html, depression.html, ptsd.html, burnout.html, stress.html

### 3C. Writing / journaling
**Target file:** `assets/inline-journal.webp`
**Unsplash query:** `person writing journal notebook soft light`
**What to look for:** Someone writing by hand, warm light, genuine mood. Not a stock pen-on-paper close-up.
**Inject on:** online-therapy-com-review.html (CBT worksheets angle), ocd.html, insomnia.html

### 3D. Couple or family moment
**Target file:** `assets/inline-couples.webp`
**Unsplash query:** `couple couch quiet close warm candid`
**What to look for:** Two people sharing a quiet moment. Warmth without staging.
**Inject on:** couples.html, relationship.html, postpartum.html

---

## TIER 4 — Forks Section Variants (Lower Priority)

Current: `video-call-earbuds.webp` used in the split/forks section across most pages.

### 4A. Forks variant
**Target file:** `assets/forks-reading.webp`
**Unsplash query:** `person reading book couch legs up relaxed`
**What to look for:** Casual, at-home, slightly lower-energy than the earbuds photo. Good for insurance/practical pages.

---

## Implementation Notes

- WCAG rule: any image with text overlay needs gradient overlay min 0.88 opacity at text position
- All hero images: landscape orientation, min 1400px wide for quality
- All inline images: portrait or square acceptable, min 800px wide
- Convert all to .webp before dropping into assets/
- After each tier is delivered, confirm with Claude and inject will begin

## Status
- [ ] Tier 1A: Homepage hero
- [ ] Tier 1B: Emotional hero (anxiety/depression cluster)
- [ ] Tier 1C: Focus hero (ADHD/burnout)
- [ ] Tier 1D: Couples hero
- [ ] Tier 1E: Teen hero
- [ ] Tier 1F: Review hero
- [ ] Tier 1G: Insurance/practical hero
- [ ] Tier 2A: Visual break couch
- [ ] Tier 2B: Visual break window
- [ ] Tier 2C: Visual break nature (optional)
- [ ] Tier 3A: Inline session
- [ ] Tier 3B: Inline relief
- [ ] Tier 3C: Inline journal
- [ ] Tier 3D: Inline couples
- [ ] Tier 4A: Forks variant
