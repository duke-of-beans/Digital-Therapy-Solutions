Execute Sprint PS-DESIGN-QA-02 — Routing Fix, Footer, Logo Accuracy, Layout Variety for Digital Therapy Solutions.
Run after PS-SEO-01 ✅ complete.

Read these files FIRST before doing anything:
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\STATUS.md
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\index.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\reviews.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\betterhelp-review.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\how-online-therapy-works.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\privacy-policy.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\templates\styles.css

Summary: After this sprint, the site will have correct Vercel routing (clean URLs, no /output/ prefix),
footer links pointing to hub pages, verified platform logos on the reviews hub, a styled
how-online-therapy-works page, privacy policy cleaned up, editorial-policy and
affiliate-disclosure confirmed live, and visual layout variety on detail pages.

---

ISSUE 1 — CRITICAL: Vercel routing — pages served at /output/ prefix

There is no vercel.json in the repo root. Vercel is serving the repo root as-is, so all
pages live at /output/page.html instead of /page.html. This breaks all clean URLs and
causes 404s on any link that doesn't include /output/.

Fix: Create vercel.json at D:\Work\Digital-Therapy-Solutions\vercel.json:

{
  "rewrites": [
    { "source": "/(.*)", "destination": "/output/$1" }
  ],
  "cleanUrls": true,
  "trailingSlash": false
}

This rewrites all requests to /output/, enables clean URLs (no .html extension),
and removes trailing slashes. After this deploys, all pages are accessible at:
  digitaltherapysolutions.com/anxiety (not /output/anxiety.html)
  digitaltherapysolutions.com/reviews
  digitaltherapysolutions.com/ → index.html

Also create output/404.html — a simple styled 404 page matching site design:
  Nav, hero with "Page not found" heading, link back to index.html.
  Follow exact HTML conventions of other output/ pages.

---

ISSUE 2 — Footer links point to detail pages, not hub pages

The footer Quick Links section across all 65 pages still links to:
  betterhelp-review.html (should be reviews.html)
  aetna.html (should be insurance.html)
  anxiety.html (not present but any condition link should go to conditions.html)

Write assets/patch_footer_links.py:
- Parse every HTML file in output/ with BeautifulSoup
- Find footer links matching these patterns and replace:
  href="betterhelp-review.html" → href="reviews.html" (in footer only)
  href="aetna.html" → href="insurance.html" (in footer only)
  href="anxiety.html" → href="conditions.html" (in footer only, if present)
- Scope to footer element only — do not change these hrefs in nav or body content
- Also update the link text:
  "Platform Reviews" label → "Platform Reviews" (keep) pointing to reviews.html
  "Insurance Guide" label → "Insurance Guide" (keep) pointing to insurance.html
- sys.stdout.reconfigure(encoding='utf-8')
Write to file before running.


---

ISSUE 3 — Reviews hub: wrong platform logos

Many logos on reviews.html are not the actual company logos — they are random scraped
images. This was flagged in PS-DESIGN-QA-01 but Clearbit was blocked in the sandbox.

Write assets/regrab-platform-logos.py:
Use Clearbit Logo API for each platform. Map platform slug to domain:

domains = {
  "adhd-online": "adhdonline.com",
  "amwell": "amwell.com",
  "bend-health": "bendhealth.com",
  "betterhelp": "betterhelp.com",
  "brightline": "hellobrightline.com",
  "brightside": "brightside.com",
  "calmerry": "calmerry.com",
  "cerebral": "cerebral.com",
  "circle-medical": "circlemedical.com",
  "doctor-on-demand": "doctorondemand.com",
  "done-adhd": "donementalhealth.com",
  "faithful-counseling": "faithfulcounseling.com",
  "gay-therapy-center": "gaytherapycenter.com",
  "grow-therapy": "growtherapy.com",
  "headspace": "headspace.com",
  "headway": "headway.co",
  "inclusive-therapists": "inclusivetherapists.com",
  "klarity": "klarityhealth.com",
  "lunajoy": "lunajoy.com",
  "manatee-health": "manatee.co",
  "mindful-care": "mindful.care",
  "nocd": "nocdtherapy.com",
  "online-therapy": "online-therapy.com",
  "open-path": "openpathcollective.org",
  "our-relationship": "ourrelationship.com",
  "our-ritual": "ouritualtherapy.com",
  "pride-counseling": "pridecounseling.com",
  "psychology-today": "psychologytoday.com",
  "regain": "regain.us",
  "simplepractice": "simplepractice.com",
  "talkiatry": "talkiatry.com",
  "talkspace": "talkspace.com",
  "teen-counseling": "teencounseling.com",
  "therapyden": "therapyden.com"
}

For each: fetch https://logo.clearbit.com/{domain}, save to assets/logos/{slug}.webp
if status 200. Log PASS/FAIL per logo. Skip if status != 200 — don't overwrite with garbage.
Use requests, sys.stdout.reconfigure(encoding='utf-8'), write to file before running.

After running: open assets/logos/ and visually verify the 5 worst offenders from the
LOGO_AUDIT.md generated in PS-DESIGN-QA-01. Check dimensions are reasonable (not 1x1 or
wildly non-square). Flag any that still look wrong in MORNING_BRIEFING.

Also fix logo display CSS: ensure all .hub-card__logo img have:
  object-fit: contain; width: 56px; height: 56px;
in styles.css. Not cover, not fill — contain only.

---

ISSUE 4 — Privacy Policy: remove attorney disclaimer sentence

Remove this exact sentence from output/privacy-policy.html:
"We're not lawyers. This policy is written in plain English, not legal boilerplate.
If you have specific legal questions about data handling, consult a qualified attorney."

Use edit_block for surgical removal. Do not rewrite the page.

---

ISSUE 5 — Confirm editorial-policy.html and affiliate-disclosure.html are accessible

Both pages exist in output/ but may not be reachable due to the Vercel routing issue
fixed in Issue 1. After Issue 1 is deployed, these will be at:
  /editorial-policy
  /affiliate-disclosure

No content changes needed — just verify they exist in output/ (they do) and that
the vercel.json fix from Issue 1 will surface them correctly.

Additionally: check that EVERY page's footer links to both pages. The footer Resources
section should contain:
  Editorial Policy → editorial-policy.html
  Affiliate Disclosure → affiliate-disclosure.html
  Privacy Policy → privacy-policy.html

Run a quick check across all pages. If any footer is missing these links, patch via
assets/patch_footer_links.py (extend the script from Issue 2).


---

ISSUE 6 — how-online-therapy-works.html needs styling

The page exists and has content but is visually unstyled — plain text with no design
treatment matching the rest of the site.

Read the full page first. Then apply the following:

1. Hero section: apply standard section-wrapper--hero pattern. If there's no hero-visual
   image, use the text-hero variant: dark bg (--bg-dark), Fraunces h1, Instrument Serif
   italic subhead, trust-row.

2. Content sections: each section (e.g. "What happens in a session", "How to get started",
   "What does it cost") should be wrapped in alternating section-wrapper / section-wrapper--alt
   divs with content-container. Section headings use .section-heading class.

3. Numbered steps: if the page has step-by-step content, apply the .timeline-list pattern
   added in PS-DESIGN-QA-01 (numbered circles in --accent-primary, connecting vertical line,
   content to right).

4. Pull quotes: add 1-2 .pull-quote blocks for strong sentences.

5. Internal links: ensure the page links to conditions.html, reviews.html, and
   how-does-pricing-work content (affordable.html or insurance.html as appropriate).

6. No inline <style> blocks. All CSS already exists in styles.css from PS-DESIGN-QA-01.

---

ISSUE 7 — Detail page layout monotony

The stacked rectangle card structure is used for every section on detail pages
(betterhelp-review.html: "Who Is BetterHelp Best For?", "Who Should Look Elsewhere?",
"Session Formats" etc. all look identical).

Apply layout variety to the 3 live review pages and top 3 insurance pages:
betterhelp-review.html, talkspace-review.html, online-therapy-com-review.html,
aetna.html, bcbs.html, cigna.html.

Rules:
- No two consecutive sections should use the same layout pattern
- Available patterns (all CSS already in styles.css from PS-DESIGN-QA-01):
  * .feature-list — vertical list with SVG bullet icons (checkmark/minus), for pros/cons
  * .split-section — 2-col: heading+text left, stat or callout right
  * .timeline-list — numbered steps with connecting line
  * .stat-callout — large DM Mono number, small label, for pricing/data sections
  * .pull-quote — Instrument Serif italic, left accent border, for strong editorial sentences
  * Standard .platform-card — keep for platform comparison sections only
  * .verdict-box — already applied in PS-DESIGN-QA-01, keep at top

Mapping guidance:
- "Who Is X Best For?" → .feature-list with checkmark SVG bullets
- "Who Should Look Elsewhere?" → .feature-list with minus SVG bullets
- "Session Formats" → .split-section (format name left, description right)
- "Pricing" → .stat-callout (price figure large, context small)
- "Our Verdict" → .verdict-box (already applied — verify still present)
- Any editorial paragraph that has a strong one-liner → .pull-quote

Apply surgically via edit_block — do not rewrite entire pages.
Read each page before editing to understand its current structure.

---

<!-- phase:execute -->

TASK: Quality gate + session close

1. Run D:\Work\Digital-Therapy-Solutions\quality_gate.py — 0 failures required.
   Page count should now be 66 (65 + 404.html).
2. Verify vercel.json exists at repo root (not in output/).
3. Spot-check 3 pages in browser after deploy:
   - Confirm /reviews loads (not /output/reviews.html)
   - Confirm footer on index.html links to reviews.html and insurance.html
   - Confirm betterhelp-review.html has visual variety between sections
4. Friction pass — FIX NOW / BACKLOG / LOG ONLY. Present before proceeding.
5. Write MORNING_BRIEFING.md to D:\Work\Digital-Therapy-Solutions\MORNING_BRIEFING.md
6. Update STATUS.md: mark PS-DESIGN-QA-02 ✅ COMPLETE with commit hash.
7. Write commit to D:\Work\Digital-Therapy-Solutions\commit-msg.txt:
   fix(routing): PS-DESIGN-QA-02 — vercel routing, footer links, logos, layout variety
8. git add . && git commit -F commit-msg.txt && git push

---

CRITICAL CONSTRAINTS:
- vercel.json goes at repo ROOT (D:\Work\Digital-Therapy-Solutions\vercel.json) — NOT in output/
- No emoji anywhere — icons-ban.md policy active
- No inline <style> blocks in any page
- Write all Python scripts to file before running (cmd 500 char limit)
- sys.stdout.reconfigure(encoding='utf-8') in every Python script
- git commit always via commit-msg.txt + git commit -F
- object-fit: contain on ALL logo img tags — never stretch or crop
- Clearbit logo grabs: only save if HTTP 200 — never overwrite with a failed/empty response

ACCEPTANCE CRITERIA:
- [ ] vercel.json exists at repo root with rewrites + cleanUrls config
- [ ] output/404.html exists and is styled
- [ ] All 65 footer instances link to reviews.html (not betterhelp-review.html)
- [ ] All 65 footer instances link to insurance.html (not aetna.html)
- [ ] All 65 footer Resources sections contain editorial-policy + affiliate-disclosure + privacy-policy links
- [ ] Platform logos re-grabbed via Clearbit, PASS/FAIL logged
- [ ] privacy-policy.html attorney disclaimer sentence removed
- [ ] how-online-therapy-works.html fully styled — hero, section wrappers, timeline
- [ ] betterhelp, talkspace, online-therapy-com review pages: no two consecutive identical section layouts
- [ ] quality_gate.py — 0 failures
- [ ] Committed and pushed — Vercel auto-deploy triggered
