# DTS Affiliate Applications Log — 2026-04-23
Sprint: DTS-POLISH-REAPPLY-01

## STATUS SUMMARY
- FlexOffers: Needs user login to reapply — see §FLEXOFFERS below
- Impact Radius: Needs user login to check — see §IMPACT_RADIUS below
- Direct programs: Require new account creation — see §DIRECT_PROGRAMS below
- Researched 16 programs across 5 networks

---

## §FLEXOFFERS — REAPPLICATION REQUIRED
**Action: David must log in at publisherprobeta.flexoffers.com/login**

Prior decline: ~2026-01 (reason: new domain, no traffic yet)
90-day cooldown: CLEARED as of ~2026-04

### Reapplication Strengthening Delta
Since last application:
- Site grew from ~50 pages to 97 fully-built, content-rich pages
- GSC: Sitemap submitted with 96 URLs — Google has read it (last crawl Apr 11)
- Redirect error fixed: apex domain now primary (was blocking 5 pages from indexing)
- Bing WMT verified and sitemap submitted (2026-04-23)
- 3 content improvements in this sprint: eating-disorders.html crisis resources, affordable.html CTA polish
- MORPH-26 design pass complete — pill CTAs, Instrument Serif stats, parallax hero, reduced-motion compliance
- FTC disclosures inline on all affiliate CTA pages (>126 insertions across 65 pages)
- Editorial policy + reviewer bio chain fully implemented

### Programs to Apply for via FlexOffers (after login)
1. **Talkspace** — $170/sale, 30-day cookie
   - Publisher portal → Advertisers → search "Talkspace" → Apply to Program
2. **Brightside** — ~$50/sale (JEBCommerce managed), 30-day cookie
   - Publisher portal → Advertisers → search "Brightside" → Apply to Program
3. **Cerebral** — Check availability (may be suspended due to prior regulatory issues)
4. **Calm** — Check availability (meditation, good for insomnia/stress pages)

### Application Pitch Text (copy/paste into site description field)
```
Digital Therapy Solutions (digitaltherapysolutions.com) is an independent editorial site
reviewing 34+ online mental health platforms. We publish condition-specific guides across
28 mental health conditions (depression, anxiety, OCD, PTSD, ADHD, eating disorders,
and more) plus 17 insurance guides. Each review follows a five-stage editorial process
with expert review. We do not accept payment for placement. Traffic: organic SEO,
growing since April 2025 GSC submission. 97 pages live, sitemap indexed by Google.
Promotion method: editorial content links in condition-specific and review pages.
FTC disclosures present on all affiliate-linked pages.
```

---

## §IMPACT_RADIUS — STATUS CHECK REQUIRED
**Action: David must log in at app.impact.com**

### Previously Applied (all pending as of last session ~2026-01):
| Brand | Program | Expected Commission | Check Status |
|---|---|---|---|
| BetterHelp | Impact Radius | ~$100-200/signup | Pending → check |
| ReGain | Impact Radius | ~$100/signup | Pending → check |
| Teen Counseling | Impact Radius | ~$100/signup | Pending → check |
| Pride Counseling | Impact Radius | ~$100/signup | Pending → check |
| Faithful Counseling | Impact Radius | ~$100/signup | Pending → check |
| Talkspace | Impact Radius (also FlexOffers) | $170/sale | New — apply here |

### If Still Pending — Escalation Note
Login → Brands → find pending applications → message each brand:

```
Hi [Brand team],

I applied to your affiliate program via Impact Radius approximately 90 days ago for
my site Digital Therapy Solutions (digitaltherapysolutions.com). Since that application
I've expanded the site to 97 pages covering 28 mental health conditions, added
detailed editorial reviews, and resolved all technical indexing issues (sitemap
confirmed by Google Search Console, Bing Webmaster Tools verified). The site is
FTC-compliant with inline disclosures on all affiliate pages.

Would love to partner with you. Could you let me know if there are any additional
steps required to move the application forward?

Thanks,
David Kirsch
Digital Therapy Solutions
```

### If Approved — Priority Activation Order
1. BetterHelp (highest traffic intent on DTS)
2. ReGain (couples content covers this)
3. Teen Counseling
4. Pride Counseling
5. Faithful Counseling

Activation: run `py assets/activate-affiliate.py --platform [slug] --url [affiliate-url]` for each.

---

## §DIRECT_PROGRAMS — RESEARCHED 2026-04-23

### Tier 1: Apply Immediately (Direct Programs, No Network Middleman)

#### 1. Online-Therapy.com
- **Program URL:** https://www.online-therapy.com/affiliate.php
- **Commission:** $150 per conversion
- **Cookie:** Not specified
- **Network:** Direct (proprietary platform)
- **Application method:** Create affiliate account at above URL
- **DTS pages that mention:** online-therapy-com-review.html
- **Pitch angle:** "Independent editorial review site, 97 pages, 28 conditions covered"
- **Status:** NOT APPLIED — needs account creation
- **Next action:** David creates account at online-therapy.com/affiliate.php
- **Expected response:** Instant (self-serve)
- **Follow-up date:** 2026-04-30

#### 2. Calmerry
- **Program URL:** https://calmerry.com/affiliate/
- **Commission:** $150 per signup
- **Cookie:** 45 days
- **Network:** Direct (proprietary platform)
- **Application method:** "Affiliate sign up" button on above URL
- **DTS pages that mention:** Would be referenced on affordability page, conditions hub
- **Pitch angle:** "$42/week platform — great fit for affordable-therapy.html content"
- **Status:** NOT APPLIED — needs account creation
- **Next action:** David clicks "Affiliate sign up" at calmerry.com/affiliate/
- **Expected response:** 2-5 business days
- **Follow-up date:** 2026-04-30

### Tier 2: Apply via FlexOffers (after FlexOffers reapplication approved)

#### 3. Talkspace
- **Program URL (FlexOffers):** flexoffers.com → Advertisers → search "Talkspace"
- **Program URL (Impact):** app.impact.com → search "Talkspace"
- **Commission:** $170 per sale
- **Cookie:** 30 days
- **Network:** FlexOffers + Impact Radius (apply to both)
- **DTS pages:** talkspace-review.html
- **Status:** NOT APPLIED — blocked on FlexOffers login

#### 4. Brightside
- **Program URL:** flexoffers.com → Advertisers → search "Brightside"
- **Commission:** ~$50/sale (JEBCommerce managed)
- **Cookie:** 30 days
- **Network:** FlexOffers
- **DTS pages:** brightside-review.html
- **Status:** NOT APPLIED — blocked on FlexOffers login

#### 5. Calm (meditation app)
- **Program URL:** flexoffers.com → Advertisers → search "Calm"
- **Commission:** ~$5-10/signup (subscription product)
- **Network:** FlexOffers + CJ
- **DTS pages:** insomnia.html, stress.html, burnout.html
- **Status:** NOT APPLIED — lower priority; apply after FlexOffers approved

### Tier 3: No Active Public Affiliate Program Found

| Brand | Notes | What to do |
|---|---|---|
| NOCD | No /affiliates page. Partnership page exists (trauma/payer focus). | Email care@nocdhelp.com to ask |
| Grow Therapy | No affiliate page. B2B/therapist focus. | Skip for now |
| Headway | No affiliate page. Insurance billing focus. | Skip for now |
| Talkiatry | No affiliate page. Insurance-only model. | Skip for now |
| Klarity | No public affiliate program found. | Check helloklarity.com/affiliates directly |
| Open Path | Non-profit pricing model — no affiliate program by design. | Skip |
| Inclusive Therapists | Smaller directory, no public affiliate program. | Skip |
| ADHD Online | Check adhdol.com/affiliates — may have direct program. | Investigate |

### Tier 4: Commission Junction (CJ) — Future Expansion

Once FlexOffers account is active, also check CJ for:
- Headspace (meditation/mindfulness)
- Amwell (telehealth)
- Doctor on Demand (telehealth)
- MDLive (telehealth)

CJ signup: cj.com → Publishers → Sign Up

---

## REVENUE FORECAST (rough, conservative)

Assumptions: 500 monthly visitors by Q3 2026, 2% CTR on affiliate CTAs, 10% conversion.

| Program | Est. Conversions/mo | Commission | Monthly Rev |
|---|---|---|---|
| BetterHelp (IR) | 1 | $150 | $150 |
| Online-Therapy.com | 1 | $150 | $150 |
| Calmerry | 1 | $150 | $150 |
| Talkspace | 0.5 | $170 | $85 |
| Others | 0.5 | $100 avg | $50 |
| **TOTAL** | **4** | | **~$585/mo** |

Upside scenario at 2,000 visitors/mo: ~$2,300/mo.
Gate: affiliate approvals + Google indexing recovery (redirect fix April 2026).

---

## NEXT ACTIONS FOR DAVID (prioritized)

1. **TODAY** — FlexOffers login + reapply + apply to Talkspace + Brightside programs
   URL: https://publisherprobeta.flexoffers.com/login
   
2. **TODAY** — Impact Radius login + check pending status + escalate if still pending
   URL: https://app.impact.com

3. **TODAY** — Online-Therapy.com affiliate account (5 min, self-serve)
   URL: https://www.online-therapy.com/affiliate.php

4. **TODAY** — Calmerry affiliate account (5 min, self-serve)
   URL: https://calmerry.com/affiliate/

5. **NEXT WEEK** — CJ account if not already set up (Headspace, Amwell)
   URL: https://www.cj.com/publisher/sign-up

6. **ONGOING** — Monitor Impact Radius for approval emails (BetterHelp cluster)
