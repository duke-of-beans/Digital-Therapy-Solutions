Execute Sprint PS-INSURANCE-01 — Insurance Logos + 17 Stub Insurer Pages for Digital Therapy Solutions.
Run after PS-CONDITIONS-01 ✅ complete.

Read these files FIRST before doing anything:
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\STATUS.md
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\BACKLOG.md
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\templates\insurance-guide.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\aetna.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\insurance.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\templates\styles.css

Summary: After this sprint, Digital Therapy Solutions will have 23 total insurer pages
(6 existing + 17 new stubs), all 17 insurer logos grabbed and stored in assets/logos/,
and insurance.html updated to display real logos across all cards. Every insurer in the
US market has an entry on the site — each is a long-tail SEO surface with internal links
back to the hub and out to relevant platform reviews. No insurer is dark.

Tasks:

1. Audit existing output/ pages to establish baseline:
   List all files in D:\Work\Digital-Therapy-Solutions\output\ and confirm the 6 live
   insurance pages: aetna.html, bcbs.html, cigna.html, unitedhealthcare.html,
   medicaid.html, affordable.html. Note their nav structure, breadcrumb pattern, and
   asset path convention (../assets/) for replication in all 17 new pages.

2. Write and run assets/grab-insurer-logos.py — logo grab script:
   Pattern: follow assets/grab-logos.py exactly. Fetch official insurer logos as WebP,
   save to assets/logos/ with filename prefix insurer- (e.g. insurer-humana.webp).

   Target insurers and their logo sources (use official brand/press pages):
   - insurer-humana.webp         → Humana
   - insurer-kaiser.webp         → Kaiser Permanente
   - insurer-anthem.webp         → Anthem
   - insurer-molina.webp         → Molina Healthcare
   - insurer-oscar.webp          → Oscar Health
   - insurer-ambetter.webp       → Ambetter
   - insurer-wellcare.webp       → WellCare
   - insurer-tricare.webp        → Tricare (Military)
   - insurer-chip.webp           → CHIP (Children's Health Insurance Program)
   - insurer-medicare.webp       → Medicare
   - insurer-beacon.webp         → Beacon Health Options
   - insurer-magellan.webp       → Magellan Health
   - insurer-centene.webp        → Centene
   - insurer-highmark.webp       → Highmark
   - insurer-harvard-pilgrim.webp → Harvard Pilgrim Health Care
   - insurer-tufts.webp          → Tufts Health Plan
   - insurer-community-health.webp → Community Health Plan

   If a logo fetch fails, log it and continue — do not block the rest of the script.
   Write script to file before running (cmd arg length limit). Use
   sys.stdout.reconfigure(encoding='utf-8') at top of script.


3. Update output/insurance.html — wire real logos into hub cards:
   The 17 stub cards on insurance.html currently use text/initial placeholders.
   Update each card to use the grabbed logo with the established fallback pattern:
     <img src="../assets/logos/insurer-humana.webp" alt="Humana logo"
          onerror="this.style.display='none';this.parentElement.textContent='H';">
   Apply to all 17 stub cards. The 6 live insurer cards should also get logo treatment
   if they don't already have it — check aetna, bcbs, cigna, unitedhealthcare, medicaid,
   affordable cards and add logo img tags where missing.
   If a logo was not successfully grabbed in Task 2, leave the initial placeholder — do
   not break the card, just skip the img tag for that insurer.

4. Build all 17 stub insurer pages — output/ directory:
   Files: humana.html, kaiser.html, anthem.html, molina.html, oscar.html,
   ambetter.html, wellcare.html, tricare.html, chip.html, medicare.html,
   beacon.html, magellan.html, centene.html, highmark.html, harvard-pilgrim.html,
   tufts.html, community-health.html

   Each page MUST match the structure of the existing live insurer pages (aetna.html
   is the reference). Use these exact conventions — no deviations:
   - DOCTYPE, charset, viewport meta — standard
   - Font links: Fraunces + Instrument Serif + DM Sans + DM Mono (same link tag as aetna.html)
   - Favicon: <link rel="icon" href="../assets/branding/favicon.png" type="image/png">
   - Stylesheet: <link rel="stylesheet" href="../templates/styles.css">
   - Nav: site-nav > site-nav__inner > site-nav__brand (href="index.html") +
     site-nav__hamburger + site-nav__links
     Nav links: Home (index.html) | Conditions (conditions.html) |
                Reviews (reviews.html) | Insurance (insurance.html) | About (about.html)
   - Breadcrumb: <nav class="breadcrumb"> Home > Insurance > [Insurer Name] </nav>
     immediately below site-nav, before the hero. Link pattern:
     <a href="index.html">Home</a> <span class="breadcrumb__sep">/</span>
     <a href="insurance.html">Insurance</a> <span class="breadcrumb__sep">/</span>
     [Insurer Name]
   - Hero: section-wrapper section-wrapper--hero with hero-visual + hero-text.
     hero-visual: use ../assets/hero.webp (same hero image used across all insurance pages)
     hero-text: insurer logo img (../assets/logos/insurer-X.webp) with onerror fallback,
     h1 headline, hero-subhead italic em, hero-subhead--follow, trust-row (4 spans)
   - Section divider SVG (copy from aetna.html exactly)
   - Main content section (section-wrapper--alt > content-container):
     h2 section-heading, then STUB CONTENT BLOCK (see below)
   - Footer: copy from aetna.html exactly
   - No inline <style> blocks — all CSS already in styles.css

   STUB CONTENT BLOCK — use this pattern for all 17 pages:
   The page should NOT be blank. It should be a real, useful stub that:
   - States clearly whether this insurer generally covers online therapy (yes/varies/limited)
   - Lists 2-3 platforms that are commonly in-network with this insurer (use real knowledge)
   - Has a "What to expect" paragraph: copay range, how to verify your specific plan
   - Has a "How to check your coverage" ordered list (3-4 steps: call member services,
     ask if telehealth mental health is covered, ask which platforms are in-network,
     confirm your deductible status)
   - Has a "More resources" section linking to: insurance.html (all insurers),
     betterhelp-review.html, talkspace-review.html (as "platforms commonly covered")
   - CTA at bottom: "Compare All Insurance Options" → insurance.html

   Headline patterns by insurer type:
   - Commercial (Humana, Anthem, Oscar, Ambetter, Highmark, Harvard Pilgrim, Tufts,
     Community Health): "Does [Insurer] Cover Online Therapy? Here's What We Know."
   - Government (Medicare, Medicaid already live, CHIP, Tricare):
     "Does [Program] Cover Online Therapy? Coverage Guide [Year]."
   - Managed behavioral (Beacon, Magellan, Centene, Molina, WellCare):
     "[Insurer] Mental Health Coverage — Online Therapy Options Explained."
   - Kaiser: "Kaiser Permanente Online Therapy — What's Covered and What Isn't."

   Write pages in batches of 3-4. Write each page to file before moving to the next.
   Do not attempt to write all 17 in a single tool call.


5. Update insurance.html — activate stub card links:
   After all 17 pages are built, update the 17 stub cards in insurance.html to link
   to their new pages. Change the card wrapper from a non-linked div to an anchor,
   or update the existing CTA href from "#" to the correct filename.
   Remove the "Coming Soon" muted state (hub-card--stub class) from all 17 cards.
   They are now live pages — treat them as live.

6. Quality gate:
   Run D:\Work\Digital-Therapy-Solutions\quality_gate.py — all pages must pass.
   If quality_gate.py needs updating to include the 17 new pages, update it first.
   Spot-check 3 new pages manually: verify nav links, breadcrumb, hero, stub content,
   footer, and no inline <style> blocks.
   Confirm insurance.html shows logos on all 23 cards (or initial fallback where logo
   grab failed — that is acceptable, blank card is not).
   All 23 insurer entries must be linked (not stubbed/greyed out).

<!-- phase:execute -->

7. Session close:
   FRICTION PASS — collect all friction from this session:
   Triage: FIX NOW / BACKLOG / LOG ONLY
   Present results before proceeding.

   MORNING_BRIEFING.md — write to D:\Work\Digital-Therapy-Solutions\MORNING_BRIEFING.md
   Schema: D:\Dev\TEMPLATES\MORNING_BRIEFING_SCHEMA.md
   Required sections: SHIPPED, QUALITY GATES, DECISIONS MADE BY AGENT,
   UNEXPECTED FINDINGS, FRICTION LOG, NEXT QUEUE

   Update STATUS.md:
   - Mark PS-INSURANCE-01 ✅ COMPLETE with commit hash
   - Update Insurance inventory: all 23 pages listed as [x]
   - Update Assets: Insurance logos ✅ (note any that failed to grab)

   Write commit message to D:\Work\Digital-Therapy-Solutions\commit-msg.txt:
   feat(insurance): PS-INSURANCE-01 — 17 insurer stub pages + logo grab

   - assets/grab-insurer-logos.py — logo fetch for 17 insurers
   - assets/logos/insurer-*.webp — insurer logos
   - output/humana.html through output/community-health.html — 17 stub pages
   - output/insurance.html — logos wired, all 23 cards now linked
   - STATUS.md updated

   Then: git add . && git commit -F commit-msg.txt && git push
   Vercel auto-deploys on push. No manual deploy step needed.

---

CRITICAL CONSTRAINTS:
- Asset paths in all output/ pages: ../assets/ (one level up from output/)
- Stylesheet path: ../templates/styles.css
- No inline <style> blocks anywhere
- No hardcoded colors — use CSS custom properties from styles.css :root
- Logo img tags MUST include onerror fallback to initials
- Write Python scripts to file before executing — never inline at cmd (500 char limit)
- sys.stdout.reconfigure(encoding='utf-8') at top of any Python script with Unicode
- git uses: cd /d D:\Work\Digital-Therapy-Solutions && git add . etc.
- All 17 pages are REAL CONTENT stubs — not empty placeholders. Each must be useful
  to a visitor who lands on it from search. Thin or blank content is not acceptable.

ACCEPTANCE CRITERIA:
- [ ] assets/grab-insurer-logos.py exists and ran; logo fetch log shows results
- [ ] assets/logos/ contains insurer-*.webp files (minimum 10 of 17 successful)
- [ ] 17 new HTML files exist in output/ matching the filenames in Task 4
- [ ] All 17 pages pass quality_gate.py
- [ ] All 17 pages have correct nav (5 links), breadcrumb, hero, stub content, footer
- [ ] No inline <style> blocks in any new page
- [ ] insurance.html shows logos on all cards that had successful logo grabs
- [ ] All 23 insurer cards on insurance.html are linked to live pages (no stubs)
- [ ] STATUS.md updated with PS-INSURANCE-01 ✅ COMPLETE + commit hash
- [ ] MORNING_BRIEFING.md written before commit
- [ ] Committed and pushed — Vercel auto-deploy triggered
