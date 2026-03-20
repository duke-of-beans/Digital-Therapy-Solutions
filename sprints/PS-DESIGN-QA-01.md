Execute Sprint PS-DESIGN-QA-01 — Design Quality + Visual Consistency Pass for Digital Therapy Solutions.
Run after PS-INSURANCE-01 ✅ complete. Independent of PS-CONDITIONS-02.

Read these files FIRST before doing anything:
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\STATUS.md
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\templates\styles.css
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\affordable.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\index.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\privacy-policy.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\reviews.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\aetna.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\betterhelp-review.html

Summary: After this sprint, the site will have consistent, polished visual design across
all page types. Unstyled content blocks will be resolved, emoji icons replaced with a
cohesive SVG icon system, insurance and platform logos used contextually throughout,
the Privacy Policy page properly typeset, an Affiliate Disclosure page created, logo
authenticity verified and corrected, and detail page layouts varied beyond repetitive
card grids. This is a CSS + HTML quality sprint — no new pages except the disclosure page.

---

ISSUE 1 — affordable.html: Unstyled list sections

The `.alternative-item` blocks under "Other Ways to Get Affordable Help" and the
`.insurance-links ul` under "Do you have insurance?" are rendering as unstyled browser-
default lists with no visual treatment. They do not match the design language of the rest
of the page.

Fix: Add CSS to templates/styles.css for these classes:

`.alternatives-list` — styled vertical list container, gap between items
`.alternative-item` — each item: left border accent in --accent-primary, padding left,
  h3 in Instrument Serif or Fraunces at appropriate weight, p in DM Sans body size.
  Subtle background: --bg-secondary. Rounded corners. No bullets.
`.insurance-links` — remove default ul list-style. Each li: inline or stacked link,
  styled as a clean text link with --accent-primary color, arrow →, hover underline.
  Optionally add a small shield/check SVG icon before each link for visual credibility.

Apply the same treatment to any other `.alternative-item` or `.insurance-links` pattern
found across other pages — do a grep for these class names across output/.


---

ISSUE 2 — Homepage condition cards: Emoji icons must be replaced

The condition tiles on index.html currently use emoji (🌊☁️⚡💑 etc.) as icons.
This is a PERMANENT ban — emoji are never acceptable on this site. They clash with the
"authoritative warmth" design language and look amateur in this context.

Replace with a cohesive inline SVG icon system. Requirements:
- Icons must be hand-drawn-feeling, single-color, stroke-based SVGs (not filled/solid)
- Stroke color: var(--accent-primary) or var(--accent-warm)
- Size: 32×32 viewBox, rendered at 28–32px
- Style: organic, slightly imperfect — humanist, not tech/SaaS
- Each condition gets a thematically appropriate icon, not a generic icon

Suggested icons per condition (implement as inline SVG in the HTML):
- Anxiety: wavy lines / ripple
- Depression: crescent moon or rain cloud (minimal strokes)
- ADHD: lightning bolt (clean stroke, not filled)
- Couples Therapy: two interlocking circles or two figures side by side
- OCD: loop/repeat arrow
- PTSD/Trauma: shield with soft interior
- Bipolar: dual arc / wave going high and low
- Eating Disorders: leaf or gentle scale
- Grief: teardrop or bare tree
- Anger: flame (minimal strokes)
- Addiction: broken chain link
- Stress: spiral
- Burnout: candle with extinguished flame
- Relationship Issues: tangled/untangled knot
- LGBTQ+: interlocking rings
- Teen Mental Health: sprout/seedling
- Postpartum: cradle or gentle arc
- Insomnia: crescent moon + star
- Chronic Pain: wave + line (body pain metaphor)
- Social Anxiety: single figure with space around them
- Phobias: eye (looking away)
- Panic: expanding concentric circles
- Loneliness: single figure
- Self-Esteem: simple star or upward arrow

IMPORTANT: Add an `icons-ban.md` note to the repo root documenting this decision:
"Emoji are permanently banned from this site. All icons must be cohesive inline SVG,
stroke-based, humanist style. Reason: emoji clash with the authoritative warmth design
language and undermine credibility. Applied first in PS-DESIGN-QA-01."

Apply the same SVG icon standard to condition cards on conditions.html hub.

---

ISSUE 3 — Insurance logos on homepage + other contextual placements

The homepage insurance tiles under "Does your insurance cover online therapy?" currently
show text-only insurer names. Insurance logos are now available at
assets/logos/insurer-*.webp. Apply them naturally wherever insurers are named.

Apply logo img tags to:
1. index.html — each insurance-tile: add insurer logo above the name, 40×40px,
   object-fit: contain. Use onerror fallback to show insurer initial letter.
2. Any other pages where an insurer is listed in a tile or card pattern — check
   insurance.html hub cards (should already have logos from PS-INSURANCE-01, verify).

Logo-to-filename mapping:
- Aetna → insurer-aetna.webp
- Blue Cross Blue Shield → insurer-bcbs.webp (or equivalent grabbed filename)
- Cigna → insurer-cigna.webp
- UnitedHealthcare → insurer-unitedhealthcare.webp (or equivalent)
- Medicaid → insurer-medicaid.webp (or equivalent)
Check actual filenames in assets/logos/ before writing — use the real filenames.

CSS: add `.insurance-tile__logo` — width: 40px, height: 40px, object-fit: contain,
margin-bottom: var(--space-xs). Add to existing .insurance-tile styles.


---

ISSUE 4 — Privacy Policy page: Typography + layout upgrade

The Privacy Policy page currently has a plain "Privacy Policy" heading in default font
and an awkward, unstyled top section. It needs a full typographic treatment to match the
rest of the site's design language.

Fix:
1. Page title h1: must use Fraunces font-family, matching the hero h1 style on other pages
2. The hero/top section: apply the standard section-wrapper--hero pattern used across the
   site — or if this page has no hero image, use a clean text-hero variant:
   dark background (--bg-dark), centered Fraunces h1, Instrument Serif italic subtitle,
   trust-row with 4 spans: "Last Updated: [date]", "Plain Language", "No Tracking", "CCPA Compliant"
3. Body content sections: wrap each section (What We Collect, How We Use It, etc.) in
   styled content blocks — use the explanation-block or similar pattern from the stylesheet.
   Add a thin --accent-primary left border to each section heading.
4. The page should feel like it belongs to this site — same nav, same footer, same
   typographic warmth — not like a dumped legal document.
5. No inline <style> blocks. All new CSS in templates/styles.css under a
   /* --- Legal Pages --- */ comment block.

---

ISSUE 5 — Affiliate Disclosure page does not exist

Create output/affiliate-disclosure.html.

This page already exists as a template but may not be in output/ or may be missing
from the nav/footer. Check:
1. Does output/affiliate-disclosure.html exist? If yes, check that it's linked from
   footer and about.html. If no, create it.
2. Content: Plain-language disclosure that the site earns commissions from affiliate
   links when readers sign up for therapy platforms. State that affiliate relationships
   never influence editorial rankings or scores. Link back to editorial-policy.html.
3. Apply the same legal page treatment from Issue 4 — matching typography and layout.
4. Ensure footer on ALL pages links to affiliate-disclosure.html. Patch via Python
   script if the link is missing — do not hand-edit 60+ pages.

---

ISSUE 6 — Logo authenticity: verification + replacement

Many platform logos in assets/logos/ are wrong — they are random images scraped instead
of actual company logos. Some are also poor resolution or have wrong aspect ratios
(e.g. Klarity logo is squished).

Approach:
1. Write assets/verify-logos.py — a verification script that:
   - Opens each WebP in assets/logos/ using PIL/Pillow
   - Checks image dimensions: flags any image where width:height ratio is outside
     0.5–3.0 (likely not a logo — too tall, too wide, or wrong shape)
   - Checks resolution: flags images under 100×100px as likely too small/low-res
   - Checks file size: flags images under 2KB as likely placeholder/failed grabs
   - Outputs a report: LOGO_AUDIT.md listing each file, dimensions, file size, and
     a PASS/FLAG status with reason
   Use sys.stdout.reconfigure(encoding='utf-8') at top.
   Write script to file before running.

2. Run the script. Review LOGO_AUDIT.md output.

3. For flagged logos: write assets/regrab-logos.py — targeted re-grab script that
   fetches logos specifically from brand press pages or Clearbit Logo API
   (https://logo.clearbit.com/{domain}) which reliably returns clean, correct logos.
   Pattern: https://logo.clearbit.com/betterhelp.com → BetterHelp logo
   Apply to all flagged platform and insurer logos.
   Save re-grabbed versions, overwriting the bad ones.

4. For Klarity specifically: re-grab and ensure the image is not squished.
   CSS fix: all .hub-card__logo and .platform-card__logo img should have
   object-fit: contain (not cover or stretch). Add this to styles.css if missing.

5. Run quality_gate.py after re-grabs to confirm no pages broke.


---

ISSUE 7 — Detail page body content: Aesthetic upgrade

The body text sections on insurance and platform detail pages (aetna.html,
betterhelp-review.html, etc.) are functional but visually flat — walls of paragraph
text with no rhythm or visual hierarchy.

Fix — add the following styled content patterns to styles.css and apply to detail pages:

a) Pull quotes: For particularly strong sentences (e.g. "Talkspace is one of the
   strongest options for Aetna members"), wrap in a `.pull-quote` block:
   Larger Instrument Serif italic text, left border in --accent-warm, subtle background
   --accent-warm-light. Not every paragraph — use sparingly, 1–2 per page.

b) Stat callouts: Where pricing or numbers appear (e.g. "$10–25/session"), wrap in
   `.stat-callout` — large DM Mono number in --accent-primary, small DM Sans label
   below. Display inline-block in a flex row of 2–3 stats.

c) Verdict box: At the top of each detail page body, a `.verdict-box` component —
   colored border, "Our Verdict" label in small caps, one-sentence summary in
   Fraunces, score badge. This replaces the current plain first paragraph.

Do NOT redesign entire pages. Apply these components surgically to existing content.
Target: betterhelp-review.html, talkspace-review.html, online-therapy-com-review.html,
aetna.html, bcbs.html, cigna.html. Other pages will pick up the CSS but don't need
manual application this sprint.

Add CSS to styles.css under /* --- Detail Page Components --- */ comment block.
Apply HTML changes via targeted edits to the 6 named pages only.

---

ISSUE 8 — Repetitive card grid layouts on detail pages

The current detail pages use the same 3-card grid for every section — Session Formats,
What We Like, Where It Falls Short all look identical. This creates visual monotony.

Fix — introduce layout variety without rebuilding pages from scratch:

a) `.feature-list` — a vertical accordion-style list (no JS needed — use pure CSS
   details/summary or just a styled definition list). Use for "What We Like" /
   "Where It Falls Short" sections: each point gets an icon bullet (inline SVG
   checkmark for positive, minus for negative), more generous line-height, subtle
   separator between items.

b) `.split-section` — a 2-column layout: left side has a heading + paragraph, right
   side has a small stat or callout box. Use for factual comparison sections.

c) `.timeline-list` — a vertical timeline for ordered information (e.g. "How to get
   started in 4 steps"): numbered circles in --accent-primary, connecting vertical
   line between them, content to the right.

Add all three patterns to styles.css under /* --- Layout Variants --- */ comment.
Apply `.feature-list` to "What We Like" / "Where It Falls Short" on betterhelp-review.html
and talkspace-review.html as proof of concept. Other pages pick up CSS but don't need
HTML changes this sprint.

---

<!-- phase:execute -->

TASK: Quality gate + session close

1. Run quality_gate.py — all 61+ pages must pass. Zero failures.
2. Spot-check in browser (python -m http.server 9000 from output/ parent):
   - affordable.html: alternatives list and insurance links styled correctly
   - index.html: SVG icons visible, no emoji anywhere
   - privacy-policy.html: Fraunces heading, styled layout
   - betterhelp-review.html: verdict box, pull quote, feature list visible
   - reviews.html: logos correct and not squished
3. Friction pass — triage all issues FIX NOW / BACKLOG / LOG ONLY.
4. Write MORNING_BRIEFING.md to D:\Work\Digital-Therapy-Solutions\MORNING_BRIEFING.md
5. Update STATUS.md: mark PS-DESIGN-QA-01 ✅ COMPLETE with commit hash.
   Add note: "Emoji permanently banned from all pages. SVG icon system established."
6. Write commit message to commit-msg.txt:
   design(qa): PS-DESIGN-QA-01 — icon system, logo audit, typography, layout variants
7. git add . && git commit -F commit-msg.txt && git push

---

CRITICAL CONSTRAINTS:
- Emoji are PERMANENTLY BANNED from this site — never use them anywhere, ever.
  Document this in icons-ban.md at repo root.
- No inline <style> blocks — all CSS in templates/styles.css
- Write Python scripts to file before running (cmd 500 char limit)
- sys.stdout.reconfigure(encoding='utf-8') in any Python script with Unicode output
- object-fit: contain on all logo img tags — never stretch or crop logos
- git commit always via commit-msg.txt + git commit -F (not -m with special chars)
- Apply HTML changes surgically — do not rewrite entire pages, only modify what's needed

ACCEPTANCE CRITERIA:
- [ ] affordable.html alternatives list and insurance links are visually styled
- [ ] index.html has zero emoji — all condition icons are cohesive inline SVGs
- [ ] conditions.html hub icons match the new SVG system
- [ ] index.html insurance tiles show insurer logos
- [ ] privacy-policy.html has Fraunces heading and styled layout
- [ ] affiliate-disclosure.html exists in output/, is linked from footer
- [ ] LOGO_AUDIT.md exists, flagged logos re-grabbed via Clearbit
- [ ] All logo img tags have object-fit: contain
- [ ] Pull quotes, stat callouts, verdict box CSS exists in styles.css
- [ ] feature-list layout applied to betterhelp and talkspace review pages
- [ ] icons-ban.md created at repo root
- [ ] quality_gate.py passes — 0 failures
- [ ] Committed and pushed — Vercel auto-deploy triggered
