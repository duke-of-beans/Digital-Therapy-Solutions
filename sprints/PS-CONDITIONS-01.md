Execute Sprint PS-CONDITIONS-01 — Condition Pages Build for Digital Therapy Solutions.
Run FIRST. No dependencies. Ready to execute immediately.

Read these files FIRST before doing anything:
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\STATUS.md
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\BACKLOG.md
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\templates\condition-guide.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\templates\styles.css
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\anxiety.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\depression.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\conditions.html

Summary: Build all 20 remaining stub condition pages. After this sprint, conditions.html
links to 24 fully-built pages (up from 4). Every condition page follows the anxiety.html
pattern exactly: empathetic hero, 3 platform recommendations with full cards, comparison
table, visual break, forks section, reviewer bio, disclaimers. The 20 stub cards in
conditions.html become live links. No structural template changes — pure content build.

---

## Condition List — 20 pages to build

The following slugs must be created in output/:

1.  ocd.html                   — OCD
2.  ptsd.html                  — PTSD / Trauma
3.  bipolar.html               — Bipolar Disorder
4.  eating-disorders.html      — Eating Disorders
5.  grief.html                 — Grief & Loss
6.  anger.html                 — Anger Management
7.  addiction.html             — Addiction & Substance Use
8.  stress.html                — Stress Management
9.  relationship.html          — Relationship Issues
10. lgbtq.html                 — LGBTQ+ Support
11. teen.html                  — Teen / Adolescent Therapy
12. postpartum.html            — Postpartum Depression
13. burnout.html               — Burnout
14. insomnia.html              — Sleep & Insomnia
15. chronic-pain.html          — Chronic Pain
16. social-anxiety.html        — Social Anxiety
17. phobias.html               — Phobias
18. panic.html                 — Panic Disorder
19. loneliness.html            — Loneliness & Isolation
20. self-esteem.html           — Self-Esteem & Confidence

---

## Content Pattern — follow anxiety.html exactly

Each page is a direct application of the condition-guide.html template. Use anxiety.html
as the gold standard — replicate its structure, quality, and tone for every condition.

### Hero section
- h1: Short, emotionally resonant. First-person lens or empathetic observation.
  Examples: "OCD isn't just about being organized." / "Grief doesn't follow a schedule."
- Subhead (italic): The unspoken experience. What it actually feels like day-to-day.
- Subhead follow: What the page delivers — "These platforms specialize in exactly that."
- Trust row: "34+ Platforms Reviewed · Expert-Written · Updated Monthly · No Sponsored Rankings"

### Platform cards — 3 per page
Use these three platforms across all pages, varying rank based on condition fit:
  BetterHelp  — best for: large network, fast matching, broad specialties
  Talkspace   — best for: insurance users, medication + therapy combo
  Online-Therapy.com — best for: structured CBT, anxiety, depression, structured programs

Rank order logic per condition:
  - CBT-responsive (OCD, PTSD, panic, social anxiety, phobias, stress, insomnia): Online-Therapy.com #1
  - Insurance-critical (postpartum, chronic pain, bipolar, eating disorders, addiction): Talkspace #1
  - Network/specialty breadth (LGBTQ+, teen, grief, burnout, loneliness, relationship, anger, self-esteem): BetterHelp #1

Card content requirements:
  - platform-card__tagline: condition-specific — why THIS platform for THIS condition
  - platform-card__body: 2 paragraphs. First: why this platform fits this condition specifically.
    Second (italic link): "Read our full [Platform] review →" linking to the review page.
  - platform-card__details: price, insurance, formats — copy exactly from anxiety.html
  - platform-card__cta: condition-aware CTA text (e.g. "Find My OCD Therapist", "Check My Insurance Coverage")
  - offer-tag: only on Online-Therapy.com ("✦ 20% off your first month") and BetterHelp ("✦ 20% off your first month")
  - rating-badge: Top Rated on #1, Recommended on #2 and #3
  - Scores: keep consistent — Online-Therapy.com: 4.8, BetterHelp: 4.5, Talkspace: 4.3

### Comparison table
Four rows: Price / Insurance / Format / Best For
Three columns: one per platform in rank order for this page.
Copy price, insurance, format values from anxiety.html — these are factual, don't vary.
Best For cell: condition-specific (e.g. "Structured CBT for OCD" not generic "Structured CBT program").

### Visual break section
- Image: ../assets/video-call-shoulder.webp (reuse across all pages)
- Quote: condition-specific, empathetic. 1–2 sentences. Attribution: "— Based on feedback from 51 platforms reviewed"

### Forks section (gentle links)
Link to 3–4 related conditions + one insurance/affordability link. Use relative links to
output/ pages. Examples for OCD.html: anxiety.html, ptsd.html, stress.html, affordable.html.
Choose forks that make sense for the condition — don't force unrelated links.

### Reviewer card
- Avatar initials: SC
- Name: Dr. Sarah Chen, LCSW
- Specialties: vary per condition appropriately (e.g. for PTSD: "Trauma · PTSD · EMDR · Anxiety Disorders")
- Bio: 2 sentences. Keep the structure of anxiety.html but adjust specialties/condition mention.

### Breadcrumb
Pattern from anxiety.html:
  <nav aria-label="Breadcrumb" class="breadcrumb" style="max-width:var(--table-width);margin:0 auto;padding:var(--space-xs) var(--space-md);">
      <a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="conditions.html">Conditions</a> / [Condition Name]
  </nav>

### Nav links — copy exactly from anxiety.html (unified nav from PS-HUB-01):
  Home → index.html
  Conditions → conditions.html
  Reviews → reviews.html
  Insurance → insurance.html
  About → about.html

### Head block — copy exactly from anxiety.html:
  - favicon + apple-touch-icon from ../assets/branding/
  - Google Fonts preconnect + full font URL (Fraunces, Instrument Serif, DM Sans, DM Mono)
  - stylesheet: ../templates/styles.css
  - meta description: unique per page, 140–160 chars, includes condition name + "online therapy" + key differentiator

### Footer — copy exactly from anxiety.html. No changes.

### JS block — copy exactly from anxiety.html. No changes.

---

## Task Breakdown

Tasks:

<!-- phase:execute -->

1. Build pages 1–5 (OCD, PTSD, bipolar, eating-disorders, grief):
   Write each to output/{slug}.html.
   Each page: full HTML from DOCTYPE to </html>. No truncation. No stubs.
   Quality check before moving to next batch:
   - No {{UNRESOLVED}} placeholders anywhere in the file
   - Nav links correct (all 5 items, correct hrefs)
   - Breadcrumb present with correct condition name
   - 3 platform cards present, ranks assigned per condition logic above
   - Comparison table present
   - Forks section links to real pages that exist in output/ or will exist this sprint
   - Reviewer card present
   - meta description unique and 140–160 chars

2. Build pages 6–10 (anger, addiction, stress, relationship, lgbtq):
   Same quality check as batch 1.

3. Build pages 11–15 (teen, postpartum, burnout, insomnia, chronic-pain):
   Same quality check as batch 1.

4. Build pages 16–20 (social-anxiety, phobias, panic, loneliness, self-esteem):
   Same quality check as batch 1.

5. Update conditions.html — convert 20 stub cards to live links:
   Read D:\Work\Digital-Therapy-Solutions\output\conditions.html.
   For each of the 20 conditions built this sprint, find the matching stub card.
   Stub cards have class "hub-card hub-card--stub" and no <a href> wrapping the card.
   Convert each stub to a live card:
   - Remove hub-card--stub class
   - Wrap card content in <a href="{slug}.html" class="hub-card__link">
   - Or match the pattern used by the 4 existing live cards (anxiety, depression, adhd, couples)
   Read the existing live card pattern first — replicate exactly, don't invent a new pattern.
   Do NOT modify anything else in conditions.html.

6. Quality gate:
   Run from D:\Work\Digital-Therapy-Solutions in cmd shell:
   python quality_gate.py
   If Python fails in cmd (ENV-001): run equivalent checks manually —
     - Count .html files in output/: should be 44 (24 was 24, +20 new)
     - Spot-check 3 random new pages: no {{PLACEHOLDER}} strings, nav correct, breadcrumb present
     - Verify conditions.html: all 24 condition cards are live (no hub-card--stub remaining)
   All checks must pass before session close.

7. Session close:

   FRICTION PASS (do this before writing MORNING_BRIEFING):
   Silently collect all friction — tool errors, content decisions that needed guessing,
   path issues, anything surprising.
   Triage: FIX NOW / BACKLOG / LOG ONLY.
   Present:
     "Session complete. 20 condition pages built, conditions.html fully live.
      Friction: [X] fixable now / [Y] to backlog / [Z] informational
      Fixable now: [list]
      Backlog: [list]
      [A] Fix now + log the rest  ← default
      [B] Just log
      [C] Skip"
   Execute chosen path.

   MORNING_BRIEFING.md — write to D:\Work\Digital-Therapy-Solutions\ BEFORE git add:
   Sections: SHIPPED / QUALITY GATES / DECISIONS MADE BY AGENT / UNEXPECTED FINDINGS /
   FRICTION LOG / NEXT QUEUE.
   NEXT QUEUE must list:
     1. PS-INSURANCE-01 — 17 stub insurer pages + logo grab
     2. PS-PLATFORMS-01 — 31 platform review pages (blocked: affiliate apps)
     3. PS-SEO-01 — meta audit, structured data, sitemap (depends on all content sprints)

   STATUS.md — update:
   - Add PS-CONDITIONS-01 row to sprint table: ✅ COMPLETE | {commit} | 2026-03-19
   - Update Conditions section: change "4 live / 24 total" to "24 live / 24 total"
   - Remove "(20 stubs — see PS-CONDITIONS-01)" note
   - Update Last Updated header

   git add + commit + push:
   Commit message via commit-msg.txt. git commit -F commit-msg.txt.
   MORNING_BRIEFING.md included in commit.
   Commit message: "PS-CONDITIONS-01: 20 condition pages built, conditions.html fully live (24/24)"

CRITICAL CONSTRAINTS:
- All 20 pages follow anxiety.html structure exactly. Template deviations require a reason.
- No {{UNRESOLVED_PLACEHOLDER}} strings in any output file — sprint fails if any remain.
- Nav on every page: 5 items, exact hrefs from anxiety.html pattern. No exceptions.
- Breadcrumb on every page: Home / Conditions / [Condition Name].
- Do NOT modify template files (templates/condition-guide.html, templates/styles.css).
- Do NOT modify any existing output/ page except conditions.html (stub → live conversion).
- Python scripts: if running .py files, use shell: "cmd" not PowerShell (ENV-001).
- MORNING_BRIEFING.md written to D:\Work\Digital-Therapy-Solutions\ BEFORE git add.
- Commit message via commit-msg.txt. Never inline.

Project: D:\Work\Digital-Therapy-Solutions
Shell: cmd (not PowerShell) for all process execution.
Git: git in PATH. cd /d D:\Work\Digital-Therapy-Solutions before any git command.
Commit via commit-msg.txt → git commit -F commit-msg.txt

ACCEPTANCE CRITERIA:
  output/ contains all 20 new .html files (ocd, ptsd, bipolar, eating-disorders, grief,
    anger, addiction, stress, relationship, lgbtq, teen, postpartum, burnout, insomnia,
    chronic-pain, social-anxiety, phobias, panic, loneliness, self-esteem)
  Zero {{PLACEHOLDER}} strings in any new file
  Every new file: correct nav (5 items), breadcrumb present, 3 platform cards, comparison
    table, forks section, reviewer card, footer, JS block
  conditions.html: all 24 condition cards are live links (zero hub-card--stub remaining)
  STATUS.md: PS-CONDITIONS-01 row added, Conditions inventory updated to 24/24
  MORNING_BRIEFING.md exists in D:\Work\Digital-Therapy-Solutions\
  All changes committed and pushed
