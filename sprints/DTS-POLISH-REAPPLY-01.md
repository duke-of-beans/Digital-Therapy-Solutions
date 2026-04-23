Execute Sprint DTS-POLISH-REAPPLY-01 — Polish + indexing verification + affiliate network reapplication for Digital Therapy Solutions.
Revenue-positive. Site is live at digitaltherapysolutions.com with 97 pages. FlexOffers declined 90 days ago (2026-01 ish), reapply window is now open. Impact Radius pending. Direct affiliate applications never attempted.

Read these files FIRST before doing anything:
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\STATUS.md
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\BACKLOG.md
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\references\DESIGN_DNA.yaml

  Discovery reads:
    ls D:\Work\Digital-Therapy-Solutions\sprints for prior sprint patterns
    grep for "affiliate" in D:\Work\Digital-Therapy-Solutions docs
    ls D:\Work\Digital-Therapy-Solutions for the MORPH-26 design files (empathetic_authority archetype)

Summary: DTS is polish-complete from MORPH-26 (Instrument Serif on score/stat numbers, pill CTAs, parallax hero, reduced-motion compliance, 6-image hero system). Sitemap submitted to GSC 2026-04-08. The gate to revenue is affiliate network approval — the site is built for affiliate revenue but has no active partners. FlexOffers declined with a 90-day cooldown (now cleared). This sprint: final polish audit + indexing verification + affiliate reapplication round.

Three tracks run serially within this sprint:

Tasks:

1. POLISH AUDIT (Engineer + Designer + Customer hats, same methodology as GAD MORPH-46):

   Run through all 97 pages looking for:
   
   Engineer hat:
     - Broken internal links (use a link checker script or grep + curl loop)
     - Missing alt text on images
     - Schema.org markup validity (MedicalCondition + FAQPage on condition pages; LocalBusiness on contact/about)
     - Broken canonical tags
     - Missing or stale lastmod on sitemap entries
     - Any remaining Lorem/placeholder/TODO content
     - Empty <head> patterns (same bug family as GAD MORPH-47-FLEET-HEAD)

   Designer hat:
     - Typography consistency (Instrument Serif on all stat/score numbers, NOT on body)
     - Pill CTAs present on all primary decision moments
     - Parallax + reduced-motion respect verified
     - WCAG overlay contrast on hero photos
     - Mobile render at 375px — any overflow, crushed text, or untappable CTAs
     - Brand tokens consistent across all 97 pages (no drift from references/DESIGN_DNA.yaml)

   Customer hat (ESPECIALLY IMPORTANT — this is a mental-health affiliate site):
     - Crisis resources visible on every condition page (suicide/self-harm adjacent topics)
     - Every condition page answers: what is it, symptoms, treatment options, when to seek help
     - No false medical claims (FDA/FTC compliance)
     - No urgency language that could manipulate vulnerable users
     - "See a professional" CTA is never far from any clinical content
     - Affiliate disclosures clear and compliant (FTC 16 CFR Part 255)
     - Privacy policy + terms actually cover affiliate relationships
     - Clear editorial policy on how partners are selected

   Write findings to D:\Work\Digital-Therapy-Solutions\_audit-notes\polish-audit-2026-04-23.md per hat.

   Fix anything trivial inline. Backlog anything requiring design decisions.

2. INDEXING VERIFICATION:

   STEP A — GSC property state:
     Log in to GSC (SA business account)
     Check digitaltherapysolutions.com property:
       - Coverage report: how many URLs indexed vs submitted?
       - Any errors (404, 5xx, soft 404, excluded)?
       - Mobile usability issues?
       - Core Web Vitals (LCP, INP, CLS) — pass or fail?
     Log findings.

   STEP B — Bing Webmaster Tools:
     Import from GSC if not already done. Check indexing status.

   STEP C — Fix any indexing blockers found:
     404s → identify broken internal links, fix
     Soft 404s → check if page is thin content, fix or deindex
     Excluded by noindex → check if intentional; if not, remove noindex
     Mobile usability → cross-reference with polish audit Designer findings
     CWV failures → identify specific pages, file focused optimization sprint if complex

   STEP D — Resubmit sitemap if anything changed during Task 1 fixes.

3. AFFILIATE REAPPLICATION ROUND:

   STEP A — FlexOffers reapply:
     The 90-day cooldown from 2026-01-XX decline is now clear.
     Login: flexoffers.com
     Update site stats if current traffic is stronger than last application
     Update site positioning to reflect the new polish + indexing story
     Submit fresh application
     Document: declined date, reapplication date, any stated reason for prior decline, application strengthening delta

   STEP B — Impact Radius follow-up:
     Previously pending — check current status
     Login: impact.com
     If still pending: escalate with a note referencing the polish + indexing improvements
     If approved: list approved brands, prioritize 5-10 for immediate link integration

   STEP C — Direct affiliate applications (new ground):
     Targets: the mental health / therapy / wellness brands DTS's content naturally mentions or recommends.
     Identify 10 candidate brands from DTS's condition pages (antidepressant manufacturers, teletherapy platforms like BetterHelp/Talkspace/Cerebral, meditation apps like Calm/Headspace, supplement brands, book publishers).
     For each: check if they run their own affiliate program (typical URL patterns: /affiliates, /partners, /ambassadors)
     Apply to each with a tailored pitch referencing DTS's editorial alignment and traffic quality.
     Log all applications to D:\Work\Digital-Therapy-Solutions\_audit-notes\affiliate-applications-2026-04-23.md with application date, contact method, expected response time, follow-up date.

   STEP D — Document affiliate readiness:
     Update D:\Work\Digital-Therapy-Solutions\AFFILIATE_STATUS.md (create if absent):
       - Which networks are active/pending/declined
       - Which direct programs are active/pending
       - Next review date for each pending application
       - Revenue forecast once approvals land (rough)

<!-- phase:execute -->

4. Portfolio compliance:
   - DTS STATUS.md: SPRINT LOG row for DTS-POLISH-REAPPLY-01
   - DTS BACKLOG.md: close polish + indexing items; open per-application follow-up reminders
   - D:\Meta\PRODUCT_GRAPH.yaml: update dts entity with affiliate_status + last_polish_date
   - D:\Ventures\Borrowed Light Group\finance\REVENUE_TRACKER.md (create if absent): note DTS as pending-revenue
   - 10 min max

5. Session close:
   FRICTION PASS: affiliate account access issues, GSC API surprises, content audit fatigue, any new blockers surfaced.
   Triage [A]/[B]/[C]. MORNING_BRIEFING.md.
   Commit + push DTS repo to its default branch.

CRITICAL CONSTRAINTS:
- DTS is a MENTAL HEALTH content site. EVERY customer hat fix gets priority over aesthetic polish.
- DO NOT add affiliate links to conditions pages without an approved partner — placeholder affiliate links are worse than no links.
- FTC compliance is NOT optional. Every affiliate-linked page needs clear disclosure in the format required by 16 CFR Part 255.
- When in doubt on medical claims language: err on the side of "may help" / "some studies suggest" / "talk to a professional." Never "cures" / "guarantees" / "clinically proven" without direct FDA-approved claim source.
- Crisis resource footer (988, Crisis Text Line) should be present on every page, not just condition pages — but check the existing pattern and follow it.
- Apply to Impact Radius's SPECIFIC brands if approved — don't just have network approval without activating links.
- MORNING_BRIEFING.md BEFORE git add.

MODEL ROUTING:
  Default: sonnet
  Task 1 Engineer: sonnet
  Task 1 Designer: sonnet
  Task 1 Customer: opus — mental health + FTC compliance requires careful judgment
  Task 2 (indexing): sonnet
  Task 3 (affiliate applications): opus — application copy + pitch framing requires judgment
  Task 4 (compliance): haiku
  Task 5 (close): sonnet

Project: D:\Work\Digital-Therapy-Solutions
Also touches: D:\Meta\PRODUCT_GRAPH.yaml, D:\Ventures\Borrowed Light Group\finance\ (may need mkdir)
Shell: cmd or powershell
Browser: Claude in Chrome for FlexOffers / Impact / GSC / direct affiliate portals

ACCEPTANCE CRITERIA:
  polish-audit-2026-04-23.md present with Engineer/Designer/Customer findings
  All HIGH audit findings fixed inline, rest backlogged clearly
  GSC coverage verified; any indexing blockers resolved or documented
  Bing WMT active
  FlexOffers reapplication submitted
  Impact Radius status updated (approved + activated, or pending with next action)
  10+ direct affiliate applications submitted with log
  AFFILIATE_STATUS.md present + current
  STATUS.md + BACKLOG.md + PRODUCT_GRAPH.yaml updated
  MORNING_BRIEFING.md in commit
  DTS repo push clean
