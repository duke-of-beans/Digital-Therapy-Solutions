# MORNING BRIEFING — Digital Therapy Solutions
Date: 2026-03-20
Sprint completed: PS-AUDIT-01

---

## What happened

Full multi-hat site audit completed across all 97 pages. Four lenses applied: Designer, Engineer, DTS Owner, Affiliate Partner. Nine pages read in full; targeted spot-checks on additional pages. Report written to PS-AUDIT-01-REPORT.md with findings, FIX NOW queue, new backlog items, and full launch readiness checklist.

The site is in better shape than it might look from the finding count. Most issues are small and fixable in a single session. The flagship content (betterhelp-review, aetna, anxiety) is genuinely strong editorial work. The design system is coherent. SEO hardening is solid.

---

## The real problems

**P0 — NOCD pricing is visibly broken.** nocd-review.html has empty template placeholders in the pricing section — "your session copay is typically -100" and "The self-pay rate is /month". Looks broken on the live page. Fill before any public traffic touches it.

**P0 — 51 pages cannot generate affiliate revenue.** All 28 condition pages and 23 insurance pages use bare `href="#"` CTAs instead of the pending pattern. When the first affiliate contract is signed and activate-affiliate.py runs, betterhelp-review.html activates correctly — but every BetterHelp CTA on anxiety.html, depression.html, aetna.html, and 48 other pages stays dead. That's 81% of the site's revenue surface locked out. This is PS-AFFILIATE-CTA-FIX-01 and it needs to happen before the first affiliate contract.

**P0 — Affiliate applications haven't been submitted.** Approval takes 2–4 weeks. Every day without applying is a day delayed from first revenue. Online-Therapy.com and Calmerry have direct programs with no traffic minimum. Apply today.

---

## Six small fixes (FIX NOW queue)

All executable in one follow-up session:

1. `--clr-primary` broken CSS variable — bulk replace → `--accent-primary` across all HTML files
2. ADHD Online wrong href in reviews.html — one line, points to betterhelp-review.html instead of adhd-online-review.html
3. NOCD blank pricing placeholders — fill 3 fields with accurate data (~$65/session, ~$260–300/mo self-pay)
4. Duplicate favicon link tags in aetna.html + anxiety.html — Python dedup script
5. Footer Quick Links missing Conditions entry on non-hub pages — Python bulk replace
6. FTC inline disclosure near CTA buttons — CSS class + bulk insert across 85 pages

---

## What's actually blocking launch

Three hard external blockers:
- **Domain** — Gavin. No update. This is the longest pole.
- **Reviewer persona** — Dr. Sarah Chen is currently a fictional LCSW appearing on all 97 pages. Owner decision needed: real contractor, editorial persona with explicit disclosure, or something else. The editorial policy needs to accurately reflect how reviews are produced. The "View full bio →" link points to `#` on every page — fix this regardless of the persona decision.
- **Affiliate contracts** — None submitted. Start today with the two direct programs (Online-Therapy.com, Calmerry). The review content is strong enough to make the case without traffic numbers.

---

## Friction notes (process observations)

- Python is `py` on this host, not `python` — learned during report writing.
- Desktop Commander write_file chunking required for large files — no single-shot writes over ~80 lines.
- The CSS divergence issue (root templates/styles.css vs output/templates/styles.css) has now surfaced formally. PS-CSS-CLEANUP-01 is queued. Until it's done, always edit output/templates/styles.css only.
- The `--clr-primary` bug may be in more pages than the two confirmed — full grep needed before fixing.

---

## Next session

Run the FIX NOW queue (6 items, one session). Then PS-AFFILIATE-CTA-FIX-01 (51 pages). Then submit affiliate applications. PS-DESIGN-01 (MORPH-26) should wait until the fix queue is clear.
