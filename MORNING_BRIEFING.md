# DTS — MORNING BRIEFING

Date: 2026-04-24 Sprint: DTS-CLEANUP-01 — COMPLETE Project: Digital Therapy Solutions (Proper Sluice Property #1) Repo: duke-of-beans/Digital-Therapy-Solutions Live: <https://digitaltherapysolutions.com>

---

## What shipped tonight

**Repo hygiene — DTS-CLEANUP-01:**

Identified 11 untracked files in `assets/` — all throwaway debug/audit scripts with hardcoded local paths and no reuse value. Added specific gitignore patterns for all of them:

- `audit2.py` through `audit5.py` — numbered iteration scripts from DTS-BUG-01 debugging
- `customer_audit.py`, `designer_audit.py` — single-use audit runs
- `fix_affordable_ct*.py` — one-off Cyrillic-filename fix script
- `fix_ed_hotline.py` — one-off hotline link fix
- `polish_audit.py`, `polish_audit_results.json` — DTS-POLISH-REAPPLY-01 debug output

`spot_check.py` (modified, tracked) — kept committed. Contains canonical/regex audit logic worth preserving.

**STATUS.md cleanup:**

- Closed stale Bing Webmaster Tools checkbox in GSC/Indexing Status (was `[ ] not yet started`; already CLOSED in Open Items since 2026-04-23)
- Bug 1 (`--clr-primary`) and Bug 2 (condition CTAs) already correctly marked `✅ RESOLVED` in Known Technical Patterns — no Open Item references to close
- Added DTS-CLEANUP-01 to Sprints table

---

## What needs David's hands today (20 min total)

### [A] FlexOffers reapplication — 10 min

URL: <https://publisherprobeta.flexoffers.com/login> 90-day cooldown CLEARED. Reapply + apply for Talkspace ($170/sale) + Brightside (~$50/sale). Pitch text: _audit-notes/affiliate-applications-2026-04-23.md §FLEXOFFERS

### [A] Impact Radius — 5 min

URL: <https://app.impact.com> Check BetterHelp / ReGain / Teen Counseling / Pride Counseling / Faithful Counseling status (applied ~Jan 2026). If approved: `py assets/activate-affiliate.py --platform [slug] --url [url]` for each.

### [B] Online-Therapy.com affiliate — 3 min

URL: <https://www.online-therapy.com/affiliate.php> $150/conversion, self-serve, instant approval.

### [B] Calmerry affiliate — 3 min

URL: <https://calmerry.com/affiliate/> $150/signup, 45-day cookie, self-serve.

---

## What's next after approvals

1. Run `py assets/activate-affiliate.py --platform [slug] --url [url]` for each approved platform
2. Run `py assets/prepare-condition-ctas.py` to verify CTA status before activating
3. DTS-CONDITION-DEEPEN-01 — deepen 28 condition pages (currently comparison-only)
4. DTS-MOBILE-01 — comparison table overflow on mobile
5. Commission Junction — Headspace, Amwell, Doctor on Demand

---

## Revenue outlook

Conservative (500 visitors/mo): ~$585/mo once approvals land Gate: affiliate approvals (site is technically ready end-to-end)

---

## Friction log (for next session)

- DC `read_file` returns metadata-only on some files — use Read tool (Filesystem MCP) as primary for reading
- Cyrillic filenames in git output are octal-escaped — glob pattern (`fix_affordable_ct*.py`) is cleaner than trying to match exact bytes in .gitignore

---

## Commit: (pending)
