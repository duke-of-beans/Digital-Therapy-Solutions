Execute Sprint PS-SEO-01 — SEO Hardening for Digital Therapy Solutions.
Run after PS-CONDITIONS-02 ✅ complete. Full content inventory is live (65 pages).

Read these files FIRST before doing anything:
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\STATUS.md
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\BACKLOG.md
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\index.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\anxiety.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\aetna.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\betterhelp-review.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\conditions.html

Summary: After this sprint, all 65 pages will have optimized meta descriptions, canonical
tags, structured data (BreadcrumbList on all pages, Review schema on platform pages,
FAQPage schema on condition/insurance pages), a generated sitemap.xml, robots.txt, and
an internal link density that gives every page a clear path back to its hub and out to
2-3 related pages. The site will be technically indexable and SEO-ready for domain
activation.

---

TASK 1 — Grab missing logo: inclusive-therapists.webp

Before SEO work, close the open asset gap from PS-CONDITIONS-02.
Write and run assets/grab-one-logo.py:

  import sys, requests, pathlib
  sys.stdout.reconfigure(encoding='utf-8')
  url = "https://logo.clearbit.com/inclusivetherapists.com"
  out = pathlib.Path("assets/logos/inclusive-therapists.webp")
  r = requests.get(url, timeout=10)
  if r.status_code == 200:
      out.write_bytes(r.content)
      print("OK:", out)
  else:
      print("FAIL:", r.status_code)

Write to file, run from D:\Work\Digital-Therapy-Solutions.
If Clearbit returns 404, try: https://logo.clearbit.com/inclusive-therapists.com
If both fail, log it and continue — don't block the sprint.

---

TASK 2 — Meta description audit + optimization (Python patch script)

Write assets/patch_meta.py — reads every HTML file in output/, checks the
<meta name="description"> tag, and flags any that are:
  - Missing entirely
  - Under 120 characters (too short)
  - Over 160 characters (gets truncated in SERPs)
  - Generic/duplicate

Output: META_AUDIT.md listing every page, current description, character count, and
PASS / SHORT / LONG / MISSING status.

After audit, write assets/fix_meta.py — applies optimized meta descriptions to all
flagged pages. Use these patterns per page type:

CONDITION PAGES — pattern: "Find the best online therapy for [condition]. Expert-reviewed
platforms, real pricing, insurance options. Updated [year]." (120–155 chars)

INSURANCE PAGES — pattern: "Does [Insurer] cover online therapy? Compare in-network
platforms, copay estimates, and how to verify your plan. Updated [year]." (130–155 chars)

REVIEW PAGES — pattern: "[Platform] review [year]: honest pros, cons, pricing, and who
it's best for. Tested by licensed therapists. No sponsored rankings." (130–155 chars)

HUB PAGES — already likely optimized, but verify and improve if short.

SUPPORTING PAGES — audit and fix individually.

Write each optimized description into the script as a dict keyed by filename.
Apply via BeautifulSoup soup.find('meta', {'name': 'description'})['content'] = new_desc
Write each file back. Use sys.stdout.reconfigure(encoding='utf-8').
Write scripts to file before running.


---

TASK 3 — Canonical tags (Python patch script)

Every page must have a canonical tag in <head>. This prevents duplicate content
penalties and signals the authoritative URL to Google.

Write assets/patch_canonicals.py:
- Reads every HTML file in output/
- Checks for existing <link rel="canonical"> tag
- If missing, inserts after the last <meta> tag in <head>
- Canonical URL pattern: https://digitaltherapysolutions.com/{filename}
  e.g. anxiety.html → https://digitaltherapysolutions.com/anxiety
  e.g. index.html → https://digitaltherapysolutions.com/ (special case)
- Use BeautifulSoup to parse and modify
- Write back to file
- Log: CANONICAL — added/already present — for each file

Run from D:\Work\Digital-Therapy-Solutions.
Write script to file before running.

---

TASK 4 — Structured data: BreadcrumbList (all pages)

Every page already has a visual breadcrumb. Add the machine-readable JSON-LD equivalent.

Write assets/patch_breadcrumb_schema.py:
- Reads every HTML file in output/ that has a breadcrumb nav
- Constructs BreadcrumbList JSON-LD based on the page's breadcrumb path:
  Home → Hub → Page (3-item list for detail pages)
  Home → Page (2-item list for hub and supporting pages)
  Home only (1-item list for index.html)
- Inserts <script type="application/ld+json"> block before </head>
- Do not duplicate if schema already present (check for existing BreadcrumbList)
- Domain: https://digitaltherapysolutions.com

Example output for anxiety.html:
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type":"ListItem","position":1,"name":"Home","item":"https://digitaltherapysolutions.com/"},
    {"@type":"ListItem","position":2,"name":"Conditions","item":"https://digitaltherapysolutions.com/conditions"},
    {"@type":"ListItem","position":3,"name":"Anxiety","item":"https://digitaltherapysolutions.com/anxiety"}
  ]
}

Build a page-to-breadcrumb map in the script covering all 65 pages.
Write script to file before running.

---

TASK 5 — Structured data: FAQPage schema (condition + insurance pages)

Condition and insurance pages contain implicit FAQ content (common questions answered
in body text). Adding FAQPage schema surfaces these as Google rich results.

Write assets/patch_faq_schema.py:
Add a FAQPage JSON-LD block to each condition page and each insurance page.
Use 3 Q&A pairs per page, derived from the page's actual content.

CONDITION PAGES — standard FAQ template (customize names inline):
  Q: "Is online therapy effective for [condition]?"
  A: "Yes — multiple studies support online therapy for [condition], with outcomes
     comparable to in-person treatment for most people."
  Q: "How much does online therapy for [condition] cost?"
  A: "Costs range from $45–100/week depending on the platform. With insurance, copays
     can bring this to $10–50/session."
  Q: "Which platform is best for [condition]?"
  A: "It depends on your needs and budget. We review 34+ platforms and recommend
     the top 3 for [condition] on this page."

INSURANCE PAGES — standard FAQ template:
  Q: "Does [Insurer] cover online therapy?"
  A: "Coverage depends on your specific plan. Many [Insurer] plans include telehealth
     mental health benefits — check with your insurer or verify at signup."
  Q: "Which online therapy platforms accept [Insurer]?"
  A: "Several platforms accept [Insurer], including Talkspace and others. The best
     options are listed on this page."
  Q: "How much will I pay for online therapy with [Insurer]?"
  A: "With in-network coverage, copays typically range from $10–50/session depending
     on your deductible and plan type."

Do not add FAQPage to hub pages, review pages, or supporting pages this sprint.
Insert before </head>. Check for existing FAQPage before inserting.
Write script to file before running.


---

TASK 6 — Structured data: Review schema (platform review pages)

The 3 existing platform review pages should have Review + AggregateRating schema.
This enables star ratings in Google search results.

Write assets/patch_review_schema.py:
Apply to: betterhelp-review.html, talkspace-review.html, online-therapy-com-review.html

BetterHelp:
{
  "@context": "https://schema.org",
  "@type": "Review",
  "itemReviewed": {"@type": "SoftwareApplication", "name": "BetterHelp",
    "applicationCategory": "Online Therapy Platform", "url": "https://www.betterhelp.com"},
  "reviewRating": {"@type": "Rating", "ratingValue": "4.5", "bestRating": "5"},
  "name": "BetterHelp Review 2026 — Honest Pros, Cons & Pricing",
  "author": {"@type": "Organization", "name": "Digital Therapy Solutions"},
  "publisher": {"@type": "Organization", "name": "Digital Therapy Solutions",
    "url": "https://digitaltherapysolutions.com"},
  "datePublished": "2026-01-01",
  "reviewBody": "BetterHelp is the largest online therapy platform with 30,000+ therapists. Strong for most people, best for those paying out of pocket without insurance needs."
}

Talkspace: ratingValue "4.3", name "Talkspace Review 2026"
reviewBody: "Talkspace is the best choice for insured clients — in-network with Aetna, Cigna, and others. Messaging-forward format suits people who prefer writing over video."

Online-Therapy.com: ratingValue "4.1", name "Online-Therapy.com Review 2026"
reviewBody: "Online-Therapy.com is built around structured CBT. Best for anxiety and depression where a clear program beats open-ended talk therapy. No insurance accepted."

Insert before </head>. Write script to file before running.

---

TASK 7 — sitemap.xml generation

Write assets/generate_sitemap.py:
- Scans all .html files in output/
- Generates a valid sitemap.xml at output/sitemap.xml
- URL pattern: https://digitaltherapysolutions.com/{filename without .html}
  Special case: index.html → https://digitaltherapysolutions.com/
- Priority assignments:
  index.html: 1.0
  Hub pages (reviews, conditions, insurance): 0.9
  Condition pages: 0.8
  Insurance pages: 0.8
  Review pages: 0.8
  Supporting pages (about, how-online-therapy-works, etc.): 0.6
  Legal pages (privacy-policy, affiliate-disclosure, editorial-policy): 0.4
- changefreq: "monthly" for all pages
- lastmod: today's date in YYYY-MM-DD format
- Output valid XML with <?xml version="1.0" encoding="UTF-8"?> header
- sys.stdout.reconfigure(encoding='utf-8')
Write to file before running.

---

TASK 8 — robots.txt

Write output/robots.txt:
  User-agent: *
  Allow: /
  Sitemap: https://digitaltherapysolutions.com/sitemap.xml

Simple, explicit, correct. Verify file exists at output/robots.txt after writing.

---

TASK 9 — Internal link density audit + patch

Every page should have meaningful links to: its hub page, and 2-3 related pages.
Pages that are islands (no internal links beyond nav) hurt crawlability and SEO.

Write assets/audit_internal_links.py:
- Parses every HTML file in output/
- Counts internal links (hrefs pointing to .html files, not external URLs)
- Excludes nav and footer links (they don't count — too generic)
- Flags pages with fewer than 3 body-content internal links
- Output: INTERNAL_LINKS_AUDIT.md — each page, link count, PASS/FLAG

After audit, review INTERNAL_LINKS_AUDIT.md. For any heavily flagged pages,
add a "Related guides" or "Also worth reading" fork section at the bottom of
the page body (above the footer) with 3 contextually relevant links.

Apply via targeted edits — do not patch all 65 pages uniformly. Focus on the
worst offenders: pages with 0-1 body content links.

Write audit script to file before running.

---

<!-- phase:execute -->

TASK 10 — Quality gate + session close

1. Run D:\Work\Digital-Therapy-Solutions\quality_gate.py — 0 failures required.
2. Spot-check 5 pages in browser (python -m http.server 9000):
   - View source on anxiety.html: confirm canonical, BreadcrumbList, FAQPage JSON-LD
   - View source on betterhelp-review.html: confirm Review schema
   - View source on aetna.html: confirm canonical, BreadcrumbList, FAQPage
   - Check output/sitemap.xml exists and is valid XML
   - Check output/robots.txt exists with correct content
3. Friction pass — triage all friction FIX NOW / BACKLOG / LOG ONLY.
   Present to user before proceeding.
4. Write MORNING_BRIEFING.md to D:\Work\Digital-Therapy-Solutions\MORNING_BRIEFING.md
   Schema: D:\Dev\TEMPLATES\MORNING_BRIEFING_SCHEMA.md
   Required sections: SHIPPED, QUALITY GATES, DECISIONS MADE BY AGENT,
   UNEXPECTED FINDINGS, FRICTION LOG, NEXT QUEUE
5. Update STATUS.md:
   - Mark PS-SEO-01 ✅ COMPLETE with commit hash
   - Add to assets: sitemap.xml ✅, robots.txt ✅
   - Note any pages that failed internal link audit (for follow-up)
6. Write commit message to D:\Work\Digital-Therapy-Solutions\commit-msg.txt:
   seo: PS-SEO-01 — canonicals, structured data, sitemap, robots, meta audit
7. git add . && git commit -F commit-msg.txt && git push

---

CRITICAL CONSTRAINTS:
- Write ALL Python scripts to file before running (cmd 500 char arg limit)
- sys.stdout.reconfigure(encoding='utf-8') at top of every Python script
- BeautifulSoup for all HTML parsing — do not use regex on HTML
- Do not hand-edit 65 pages — everything via script
- No inline <style> blocks in any page
- git commit always via commit-msg.txt + git commit -F
- Domain for all schema/canonical/sitemap: https://digitaltherapysolutions.com
  (Note: domain not yet live — use this as the target domain consistently)

ACCEPTANCE CRITERIA:
- [ ] assets/logos/inclusive-therapists.webp exists (or failure logged)
- [ ] META_AUDIT.md generated, all pages at 120–160 chars
- [ ] All 65 pages have <link rel="canonical"> in <head>
- [ ] All 65 pages have BreadcrumbList JSON-LD
- [ ] All 28 condition pages have FAQPage JSON-LD
- [ ] All 23 insurance pages have FAQPage JSON-LD
- [ ] 3 review pages have Review + AggregateRating JSON-LD
- [ ] output/sitemap.xml exists, valid XML, all 65 pages included
- [ ] output/robots.txt exists with Allow: / and Sitemap directive
- [ ] INTERNAL_LINKS_AUDIT.md generated, worst offenders patched
- [ ] quality_gate.py — 0 failures
- [ ] STATUS.md updated, commit hash logged
- [ ] MORNING_BRIEFING.md written before commit
- [ ] Committed and pushed — Vercel auto-deploy triggered
