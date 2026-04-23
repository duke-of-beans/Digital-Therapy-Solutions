# Digital Therapy Solutions — AFFILIATE STATUS
Last Updated: 2026-04-23 (DTS-POLISH-REAPPLY-01)

## Network Status

| Network | Status | Account | Notes |
|---|---|---|---|
| FlexOffers | ⚠️ REAPPLY NEEDED | publisherprobeta.flexoffers.com | Declined ~2026-01 (no traffic). 90-day cooldown cleared. Login to reapply. |
| Impact Radius | ⏳ PENDING | app.impact.com | Applied 2026-01. BetterHelp cluster pending. Login to check + escalate. |
| Commission Junction (CJ) | ❌ NOT STARTED | cj.com | Future: Headspace, Amwell, Doctor on Demand |
| ShareASale | ❌ NOT STARTED | shareasale.com | Future: research what mental health programs are on this |

## Direct Program Applications

| Brand | Commission | Status | URL | Next Action |
|---|---|---|---|---|
| Online-Therapy.com | $150/conv | ❌ NOT APPLIED | online-therapy.com/affiliate.php | Create account (self-serve) |
| Calmerry | $150/signup | ❌ NOT APPLIED | calmerry.com/affiliate/ | Create account (5 min) |
| Talkspace | $170/sale | ❌ NOT APPLIED | Via FlexOffers + Impact | Apply after FO approved |
| Brightside | ~$50/sale | ❌ NOT APPLIED | Via FlexOffers | Apply after FO approved |
| BetterHelp | ~$150/signup | ⏳ PENDING | Via Impact Radius | Check IR dashboard |
| ReGain | ~$100/signup | ⏳ PENDING | Via Impact Radius | Check IR dashboard |
| Teen Counseling | ~$100/signup | ⏳ PENDING | Via Impact Radius | Check IR dashboard |
| Pride Counseling | ~$100/signup | ⏳ PENDING | Via Impact Radius | Check IR dashboard |
| Faithful Counseling | ~$100/signup | ⏳ PENDING | Via Impact Radius | Check IR dashboard |

## No Affiliate Program
| Brand | Reason |
|---|---|
| NOCD | No public affiliate program — contact care@nocdhelp.com to inquire |
| Grow Therapy | B2B/therapist focused, no publisher affiliate program |
| Headway | Insurance billing focus, no publisher affiliate program |
| Talkiatry | Insurance-only, no publisher affiliate program |
| Open Path | Non-profit pricing, no affiliate program by design |

## Indexing Readiness for Affiliate Links
When programs are approved, run `activate-affiliate.py` to replace `cta-button--pending` with live links:
```
py assets/activate-affiliate.py --platform [slug] --url [affiliate-url]
```

Pending patterns currently active on:
- betterhelp-review.html (3 CTAs)
- talkspace-review.html (3 CTAs)
- All 34 review pages (data-affiliate-status="pending")
- affordable.html (3 CTAs — fixed in DTS-POLISH-REAPPLY-01)

## Revenue Forecast
Conservative (500 visitors/mo): ~$585/mo once approvals land
Upside (2,000 visitors/mo): ~$2,300/mo

Gate to revenue: affiliate approvals + Google indexing (redirect fix 2026-04-23)

## Next Review Date
2026-05-07 — Check Impact Radius approval status for BetterHelp cluster
2026-04-30 — Confirm FlexOffers reapplication submitted + Direct programs applied
