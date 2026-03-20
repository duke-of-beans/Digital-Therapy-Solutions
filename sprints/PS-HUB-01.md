# Sprint PS-HUB-01 — Hub Pages + Nav Update
**Project:** Digital Therapy Solutions (Proper Sluice #1)
**Repo:** D:\Work\Digital-Therapy-Solutions
**Sprint:** PS-HUB-01
**Status:** READY

---

## Problem

The site nav currently deep-links directly to single pages:
- "Conditions" → `anxiety.html`
- "Reviews" → `betterhelp-review.html`
- "Insurance" → `aetna.html`

Users land on one page with no way to discover the rest. The site has 4 condition pages,
3 review pages, and 5 insurance pages — none of them discoverable from each other.
Long-term the site will have 34 platform pages, 20+ condition pages, and 15–20 insurance
pages. All of it needs an indexing layer.

---

## Deliverables

### 1. `output/reviews.html` — Platform Reviews Hub

**Hero headline:** "We tested 34+ online therapy platforms. Here's our honest take on each."
**Hero subhead (italic):** *"No sponsored rankings. No affiliate influence on scores. Just what we found."*

**Body:** Introductory paragraph (2–3 sentences) explaining the review methodology — hands-on
testing, no pay-to-rank.

**Card grid:** One card per platform logo found in `assets/logos/`. For the 3 platforms with
full review pages (BetterHelp, Talkspace, Online-Therapy.com), the card CTA links to the
review page. For all others, the card is marked "Review Coming" with a grayed CTA — the card
is visible and the logo is shown, but no page link yet.

Each card contains:
- Platform logo from `assets/logos/[platform].webp`
- Platform name
- One-line descriptor (e.g. "Best for: therapist matching flexibility")
- CTA button: "Read Review" (live) or "Coming Soon" (stub, visually muted)

Grid: 3-across desktop, 2-across tablet, 1-across mobile.

**Full platform list to card (match to logo filenames in assets/logos/):**
adhd-online, amwell, bend-health, betterhelp, brightline, brightside, calmerry, cerebral,
circle-medical, doctor-on-demand, done-adhd, faithful-counseling, gay-therapy-center,
grow-therapy, headspace, headway, inclusive-therapists, klarity, lunajoy, manatee-health,
mindful-care, nocd, online-therapy, open-path, our-relationship, our-ritual,
pride-counseling, psychology-today, regain, simplepractice, talkiatry, talkspace,
teen-counseling, therapyden
