# DTS — MORNING BRIEFING
Date: 2026-04-23
Sprint: DTS-POLISH-REAPPLY-01 — COMPLETE
Project: Digital Therapy Solutions (Proper Sluice Property #1)
Repo: duke-of-beans/Digital-Therapy-Solutions
Live: https://digitaltherapysolutions.com

---

## What shipped tonight

**Indexing:**
- Fixed the Vercel apex/www redirect error blocking 5 pages from Google indexing (depression, anxiety, betterhelp-review, nocd-review, reviews). Apex is now Production; www redirects to apex. All 5 pages resubmitted to GSC priority crawl queue.
- Bing Webmaster Tools: site added, verified (msvalidate meta tag on index.html), sitemap submitted 2026-04-23.

**Polish fixes (3 pages):**
- affordable.html: 3 dead `btn btn-primary` CTAs replaced with proper `cta-button--pending` pattern (FTC compliant)
- eating-disorders.html: crisis resource block inserted before reviewer bio (Alliance 1-866-662-1235, Crisis Text Line, 988)
- index.html: Bing WMT msvalidate meta tag added

**Docs created:**
- _audit-notes/polish-audit-2026-04-23.md — full three-hat audit (Engineer/Designer/Customer)
- _audit-notes/affiliate-applications-2026-04-23.md — research log for 16 affiliate programs with pitch text
- AFFILIATE_STATUS.md — network/program tracking doc with revenue forecast

**Portfolio updated:** STATUS.md, BACKLOG.md, PRODUCT_GRAPH.yaml, REVENUE_TRACKER.md

---

## What needs David's hands today (20 min total)

### [A] FlexOffers reapplication — 10 min
URL: https://publisherprobeta.flexoffers.com/login
90-day cooldown from Jan decline is CLEARED. Reapply + apply for:
  - Talkspace ($170/sale)
  - Brightside (~$50/sale)
Pitch text ready: _audit-notes/affiliate-applications-2026-04-23.md §FLEXOFFERS

### [A] Impact Radius — 5 min
URL: https://app.impact.com
Check BetterHelp / ReGain / Teen Counseling / Pride Counseling / Faithful Counseling status (applied ~Jan 2026).
If still pending: escalation note ready in affiliate log.
If approved: run `py assets/activate-affiliate.py --platform [slug] --url [url]` for each.

### [B] Online-Therapy.com affiliate — 3 min
URL: https://www.online-therapy.com/affiliate.php
$150/conversion, self-serve, instant approval. Create account.

### [B] Calmerry affiliate — 3 min
URL: https://calmerry.com/affiliate/
$150/signup, 45-day cookie, self-serve. Click "Affiliate sign up".

---

## What's next after approvals

1. Run activate-affiliate.py for each approved platform → CTAs go live site-wide
2. Resubmit sitemap (GSC) after CTA text changes
3. DTS-CONDITION-DEEPEN-01 — deepen the 28 condition pages (currently comparison-only)
4. DTS-MOBILE-01 — comparison table overflow on mobile
5. Commission Junction account — Headspace, Amwell, Doctor on Demand

---

## Revenue outlook
Conservative (500 visitors/mo): ~$585/mo once approvals land
Gate: affiliate approvals + Google indexing recovery
Indexing timeline: Google typically re-crawls priority queue within 1-7 days

---

## Audit findings backlogged (not blocking)
- 28 condition pages comparison-only — no first-person symptom descriptions (DTS-CONDITION-DEEPEN-01)
- Reviewer persona still generic placeholder — needs David decision (name/credentials or editorial policy link only)
- Mobile comparison table overflow still present (DTS-MOBILE-01)

---

## Commit: 8201e1a (2026-04-23)
Files: affordable.html, eating-disorders.html, index.html, _audit-notes/polish-audit-2026-04-23.md
