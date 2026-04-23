# DTS Polish Audit — 2026-04-23
Sprint: DTS-POLISH-REAPPLY-01
Pages audited: 97 HTML files (output/)
Date: 2026-04-23

---

## ENGINEER HAT

### CLEAN

- Broken internal links: 0
- Alt text: All non-decorative images correct. site-nav__brand-icon alt="" is correct WCAG (decorative + companion text).
- Canonical tags: All 97 pages. Format: href="..." rel="canonical" (correct).
- Schema.org: All real pages have JSON-LD. fo-verify.html exempt (not user-facing).
- Meta descriptions: All 97 pages. Format: content="..." name="description".
- Sitemap coverage: All 97 pages (clean URLs, no .html extension). GSC-submitted 2026-04-08.
- --clr-primary CSS bug: CONFIRMED FIXED. 0 occurrences remaining.
- Noindex: 0 pages.
- Crisis 988 + CTL: Present in footer on all user-facing pages.
- FTC disclosure on review pages: All 34 review pages — inline text + link to affiliate-disclosure.html.

### FINDINGS

[FIX NOW — MEDIUM] affordable.html — 3 dead CTAs using wrong class + href="#"
Platform cards use <a class="btn btn-primary" href="#"> instead of cta-button--pending pattern.
Platforms affected: Open Path, BetterHelp, Online-Therapy.com.
activate-affiliate.py cannot reach these. Users dead-ended on click.
Fix: Replace with cta-button cta-button--pending + data-affiliate-status="pending" + data-platform per slug.

[KNOWN P1 — BACKLOG] Reviewer bio links: href="#" on all 97 pages.
View full bio still points nowhere. Pre-existing PS-REVIEWER-BIO-01, blocked on persona decision.

[LOW — BACKLOG] about.html + do-i-need-therapy.html: no cta-button element.
Informational pages with text links only. Could add Find a therapist CTA to reviews.html.

---

## DESIGNER HAT

### CLEAN

- Pill CTAs: --cta-radius: 100px in :root, applied to .cta-button. All primary CTAs pill-shaped.
- Instrument Serif on stats: --font-display: 'Instrument Serif' in :root. .score-number and .stat-callout__number both use font-family: var(--font-display).
- Reduced-motion: Two @media (prefers-reduced-motion: reduce) blocks. Animations suppressed. .reveal elements set visible with no transform.
- Parallax + reduced-motion: Parallax JS on all tested pages. Inline prefers-reduced-motion check present.
- WCAG overlay gradient: .visual-break__overlay uses rgba(0,0,0,0.15) to rgba(0,0,0,0.55) bottom-weighted. Sufficient contrast.
- Design tokens: :root complete. --accent-primary: #2D7A6F, --cta-radius: 100px, all font/spacing/shadow/crisis tokens present. No drift.

### FINDINGS

[P2/KNOWN — BACKLOG] Platform logo placeholders: hardcoded hex in inline styles.
Review + insurance pages use inline background hex (#009688, #1976D2, etc.) for platform logo boxes.
Pre-existing Clearbit DNS issue (PS-LOGO-REFRESH-01). Not a brand token violation but visually inconsistent.

[NOT VERIFIED] Mobile 375px: No screenshot verification this sprint.
PS-MOBILE-01 (comparison table overflow) remains queued.

---

## CUSTOMER HAT

### CLEAN

- Crisis resources: 988 + CTL in site footer on every page. Format: In crisis? Call or text 988 . Text HOME to 741741 . Emergency: 911.
- False medical claims: None. No cures/guarantees/clinically proven/FDA-approved language on checked pages.
- Urgency/manipulative language: None. No limited time/act now/only N left on any page.
- FTC inline: All review pages have affiliate disclosure inline + affiliate-disclosure.html link.
- Privacy policy: Includes Affiliate tracking as named third-party category.
- Professional advice CTAs: At least 1 per condition page checked.

### FINDINGS

[FIX NOW — HIGH] eating-disorders.html: No eating-disorder-specific hotline.
The page has 988 + CTL in the footer but no dedicated eating disorder crisis line.
NEDA (National Eating Disorders Association) helpline is permanently disconnected.
Fix: Add National Alliance for Eating Disorders helpline 1-866-662-1235 to the page content.
Reference: https://www.allianceforeatingdisorders.com/

[HIGH — BACKLOG] Condition pages: comparison-only, no educational health content.
Sprint requirement: every condition page answers what is it, symptoms, treatment options, when to seek help.
Current reality: condition pages are structured as platform recommendation/comparison pages only.
Example: anxiety.html headings are Platforms We Recommend for Anxiety, About Our Editorial Process.
No what-is, no symptoms, no treatment options, no when-to-seek-help sections on any tested page.
This is a structural gap, not a trivial inline fix. Scope as PS-CONDITION-CONTENT-01.
Impact: reduced credibility for affiliate partners, reduced SEO depth, FTC risk if site reads as pure ad without informational value.

[MEDIUM — BACKLOG] crisis-resources.html not linked from condition pages.
The dedicated crisis-resources.html page is only linked from index.html.
No condition page links to it. The footer 988/CTL text is good but the resource page adds depth for users in acute distress.
Fix: Add crisis-resources.html link to footer Quick Links or condition page body on all 28 condition pages.

[MEDIUM — VERIFY] Editorial policy and partner selection transparency.
affiliate-disclosure.html and editorial-policy.html exist and are linked from every page footer.
Content not fully spot-checked in this sprint. Manual review recommended before FlexOffers reapplication — affiliate networks often check these pages.

---

## INLINE FIXES APPLIED THIS SPRINT

1. affordable.html — 3 dead CTAs updated to cta-button--pending pattern (see below)
2. eating-disorders.html — National Alliance for Eating Disorders hotline added

---

## BACKLOG ADDITIONS FROM THIS AUDIT

PS-CONDITION-CONTENT-01 [HIGH] — Add what-is/symptoms/treatment/when-to-seek sections to all 28 condition pages.
PS-CRISIS-LINK-01 [MEDIUM] — Add crisis-resources.html link to condition page footers.
PS-MOBILE-VERIFY-01 [MEDIUM] — Screenshot verification at 375px (comparison tables + all page types).
PS-ABOUT-CTA-01 [LOW] — Add primary CTA to about.html and do-i-need-therapy.html.
