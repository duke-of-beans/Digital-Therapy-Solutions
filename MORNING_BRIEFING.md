# DTS — MORNING BRIEFING
Date: 2026-04-24
Sprint: DTS-BUG-01 — COMPLETE
Project: Digital Therapy Solutions (Proper Sluice Property #1)
Repo: duke-of-beans/Digital-Therapy-Solutions
Live: https://digitaltherapysolutions.com

---

## What shipped tonight

**Bug 1 — CSS `--clr-primary` alias:**
Added `--clr-primary: var(--accent-primary);` to `:root` in `output/templates/styles.css`. The variable was not referenced in any current HTML (prior sprints had already cleaned up inline usage), but the alias is now defined as defensive CSS. Teal value: `#2D7A6F`.

**Bug 2 — Affiliate activation robustness:**
`activate-affiliate.py` Pattern 3 (legacy pending CTA match) was using a rigid attribute-order regex that would miss `affordable.html`'s 3 pending CTAs. Fixed with lookahead-based order-independent matching. Dry-run confirmed all 3 now activate correctly. Condition/insurance pages (90 CTAs) already use `data-affiliate-status="direct"` from PS-AFFILIATE-CTA-FIX-01 — handled by Patterns 1+2 unchanged.

New tool: `assets/prepare-condition-ctas.py` — audit script for CTA status across all non-review pages. Run any time before affiliate activation. Detects bare `href="#"` CTAs and can fix them with `--fix` flag.

**Site state:** 0 bare `href="#"` CTAs remain. 90 direct CTAs + 3 pending (affordable.html) = 93 affiliate-ready CTAs across condition/insurance pages.

---

## What needs David's hands today (20 min total)

### [A] FlexOffers reapplication — 10 min
URL: https://publisherprobeta.flexoffers.com/login
90-day cooldown CLEARED. Reapply + apply for Talkspace ($170/sale) + Brightside (~$50/sale).
Pitch text: _audit-notes/affiliate-applications-2026-04-23.md §FLEXOFFERS

### [A] Impact Radius — 5 min
URL: https://app.impact.com
Check BetterHelp / ReGain / Teen Counseling / Pride Counseling / Faithful Counseling status (applied ~Jan 2026).
If approved: `py assets/activate-affiliate.py --platform [slug] --url [url]` for each.

### [B] Online-Therapy.com affiliate — 3 min
URL: https://www.online-therapy.com/affiliate.php
$150/conversion, self-serve, instant approval.

### [B] Calmerry affiliate — 3 min
URL: https://calmerry.com/affiliate/
$150/signup, 45-day cookie, self-serve.

---

## What's next after approvals

1. Run `py assets/activate-affiliate.py --platform [slug] --url [url]` for each approved platform
2. Run `py assets/prepare-condition-ctas.py` to verify CTA status before activating
3. DTS-CONDITION-DEEPEN-01 — deepen 28 condition pages (currently comparison-only)
4. DTS-MOBILE-01 — comparison table overflow on mobile
5. Commission Junction — Headspace, Amwell, Doctor on Demand

---

## Revenue outlook
Conservative (500 visitors/mo): ~$585/mo once approvals land
Gate: affiliate approvals (site is technically ready end-to-end)

---

## Friction log (for next session)
- DC `start_process` wraps inline `python -c "..."` in extra quotes. Always write to a `.py` file and run it.
- `findstr` cannot search `--` CSS variable prefixes in cmd (exits 1). Use Python for CSS variable lookups.

---

## Commit: pending
