\# Digital Therapy Solutions — [STATUS.md](http://STATUS.md)Last Updated: 2026-04-24 (DTS-CLEANUP-01 — gitignore throwaway audit scripts, close resolved STATUS items)

## Sprints

SprintNameStatusCommitPS-PROP-01Initial build — 21 pages✅ COMPLETE(initial)PS-PROP-01-FIXNav/CSS unification — 9 pages fixed✅ COMPLETE590a427PS-HUB-01Hub pages + nav update + breadcrumbs✅ COMPLETEe4a7211PS-CONDITIONS-0120 condition pages + conditions.html fully live (24 cards)✅ COMPLETE889f7dcPS-INSURANCE-0117 insurer logos + 17 stub pages + insurance.html all live✅ COMPLETEb90b345PS-DESIGN-QA-01Design quality pass — icons, logos, typography, layout variants✅ COMPLETE682bb37PS-CONDITIONS-024 remaining condition pages — conditions vertical 28/28✅ COMPLETE16ad1e8PS-SEO-01Canonicals, structured data, sitemap, robots, meta audit✅ COMPLETE1094e09PS-DESIGN-QA-02Vercel routing, footer links, logos, layout variety✅ COMPLETE27a767dPS-ROUTING-FIXvercel.json outputDirectory — clean URLs confirmed live✅ COMPLETEdb10564PS-PLATFORMS-0131 review pages + affiliate toggle system✅ COMPLETE463301ePS-AUDIT-01Full multi-hat site audit — Designer/Engineer/Owner/Affiliate✅ COMPLETE—PS-DESIGN-01MORPH-26 design intelligence pass✅ COMPLETE573bfadPS-AFFILIATE-CTA-FIX-01CTA direct links + CSS fix — 93 CTAs live, 0 dead✅ COMPLETE—PS-CONTENT-ENRICH-0110 priority review pages enriched to flagship depth✅ COMPLETE1584ae5PS-IMAGE-01Hero image replacement + 6-image variation system✅ COMPLETEfaafe00PS-SEO-GSC-01Sitemap updated (96 URLs, 2026-04-08) + submitted to GSC✅ COMPLETE8609018DTS-POLISH-REAPPLY-01Three-hat polish audit + indexing fixes + affiliate reapplication research✅ COMPLETE8201e1aDTS-BUG-01CSS --clr-primary alias + [activate-affiliate.py](http://activate-affiliate.py) Pattern 3 robustness✅ COMPLETEbdce63eDTS-CLEANUP-01gitignore throwaway audit scripts + close resolved STATUS items✅ COMPLETE—

## PS-AUDIT-01 Notes

- Full multi-hat audit complete — 9 pages read in full, targeted spot-checks across all 5 verticals
- Report: [PS-AUDIT-01-REPORT.md](http://PS-AUDIT-01-REPORT.md)
- P0 findings: NOCD blank pricing (nocd-review.html), condition/insurance CTAs not using pending pattern (51 pages), [activate-affiliate.py](http://activate-affiliate.py) only covers review pages
- P1 findings: `--clr-primary` broken variable (renders blue not teal), ADHD Online wrong href in reviews.html, footer missing Conditions link on non-hub pages, FTC inline disclosure gap, reviewer bio link dead on all 97 pages, 31 new review pages are thin vs flagship depth
- New backlog items added: PS-AFFILIATE-CTA-FIX-01 (P0), PS-CONTENT-ENRICH-01 (P1), PS-REVIEWER-BIO-01 (P1), PS-CSS-CLEANUP-01 (P1), PS-AFFILIATE-OUTREACH-01 (P0), PS-CEREBRAL-REVIEW (P1)
- Launch readiness: NOT YET — domain (Gavin), reviewer persona decision, affiliate applications are hard external blockers
- FIX NOW queue: 6 items, all executable in &lt;3 tool calls each — see report

## PS-PLATFORMS-01 Notes

- 31 new review pages built — all follow betterhelp-review.html structure
- All 34 review pages (including 3 existing) use data-affiliate-status="pending" pending CTA pattern
- assets/activate-affiliate.py ready: py assets/activate-affiliate.py --platform \[slug\] --url \[url\]
- .cta-button--pending CSS added to templates/styles.css
- reviews.html: all 34 cards live-linked, 0 stubs
- output/sitemap.xml regenerated: 97 URLs
- Quality gate: 0 failures, 97 pages

## PS-DESIGN-QA-02 Notes

- vercel.json at repo root — clean URLs live (/reviews, /betterhelp-review, etc.)
- output/404.html — styled 404 page added
- Footer links patched on 62 pages — Quick Links now → reviews.html + insurance.html
- Platform logo Clearbit regrab: 0/34 PASS (DNS blocked on host — backlogged)
- .hub-card__logo img: object-fit: contain fixed in styles.css
- privacy-policy.html: attorney disclaimer removed
- how-online-therapy-works.html: fully restyled (hero, timeline, split-section, stat-callouts)
- Layout variety applied to 6 detail pages (betterhelp, talkspace, online-therapy-com, aetna, bcbs, cigna)
- Quality gate: 0 failures, 66 pages

## PS-SEO-01 Notes

- Meta descriptions: 65/65 at 120-160 chars (23 were flagged, all fixed)
- Canonicals: 65/65 pages
- BreadcrumbList JSON-LD: 65/65 pages
- FAQPage JSON-LD: 28 condition + 23 insurance pages
- Review JSON-LD: BetterHelp (4.5★), Talkspace (4.3★), [Online-Therapy.com](http://Online-Therapy.com) (4.1★)
- sitemap.xml: 65 URLs, priority tiers, valid XML
- robots.txt: Allow: /, Sitemap directive
- Internal links: 65/65 pages ≥3 body links (4 pages patched: privacy-policy, about, affiliate-disclosure, editorial-policy)
- Quality gate: 0 failures

## Open Items

- P0: FlexOffers reapply — David must login to [publisherprobeta.flexoffers.com](http://publisherprobeta.flexoffers.com) and reapply. 90-day cooldown CLEARED. Apply for Talkspace + Brightside programs while there. Pitch text ready in \_audit-notes/affiliate-applications-2026-04-23.md
- P0: Impact Radius — David must login to [app.impact.com](http://app.impact.com) to check BetterHelp cluster status (applied \~2026-01). Escalation note ready in affiliate applications log.
- P0: [Online-Therapy.com](http://Online-Therapy.com) affiliate signup — Direct, $150/conv, 5 min: [online-therapy.com/affiliate.php](http://online-therapy.com/affiliate.php)
- P0: Calmerry affiliate signup — Direct, $150/signup, 45-day cookie: [calmerry.com/affiliate/](http://calmerry.com/affiliate/)
- P1: Commission Junction — not yet started (Headspace, Amwell, Doctor on Demand): [cj.com](http://cj.com)
- P2: PS-MOBILE-01 — comparison table overflow on mobile (queued)
- P2: PS-DTS-EQUITABLE-01 — image slots in all section templates (deferred)
- ✅ CLOSED: Bing Webmaster Tools — verified + sitemap submitted 2026-04-23
- ✅ CLOSED: GSC redirect error — Vercel apex/www fixed 2026-04-23, 5 pages resubmitted
- ✅ CLOSED: Backlog reviewer bio link — fixed in DTS-POLISH-REAPPLY-01
- ✅ CLOSED: eating-disorders.html missing crisis hotline — fixed in DTS-POLISH-REAPPLY-01
- ✅ CLOSED: affordable.html dead CTAs — converted to pending pattern in DTS-POLISH-REAPPLY-01

## PS-CSKY Session Improvements (2026-04-03) — Principles applied in PS-DESIGN-01

- \[x\] **PS-DTS-BUTTON-01** — CTA pill shape: --cta-radius changed from 8px to 100px site-wide
- \[x\] **PS-DTS-FONT-01** — Typography warmth: score-number + stat-callout__number switched from DM Mono to Instrument Serif; stat callout size bumped to clamp(2.5rem,5vw,4rem)
- \[x\] **PS-DTS-WCAG-01** — WCAG photo surfaces: gradient overlay added to .visual-break__overlay (bottom-weighted 0.55 at bottom); text-shadow on .visual-break__quote
- \[x\] **PS-DTS-ANIM-01** — Smart animations: statSpring keyframe, heroEntrance stagger, visual break parallax JS on 43 pages, prefers-reduced-motion compliance
- \[x\] **PS-DTS-RHYTHM-01** — Emotional rhythm: visual breaks added to autism, life-transitions, mens-mental-health, womens-mental-health
- \[x\] **PS-DTS-REINFORCE-01** — Decision reinforcement: .cta-reassurance CSS class added to styles.css
- \[x\] **PS-DTS-ICON-01** — Icon system: emoji ban holding (confirmed audit), stroke SVG standard in place
- \[ \] **PS-DTS-EQUITABLE-01** — Equitable visuals: image slots in all section templates (deferred — requires section template rebuild, scope for next sprint)

## Known Technical Patterns

- Python inline commands via cmd fail at \~500+ chars — always write to file first
- sys.stdout.reconfigure(encoding='utf-8') is correct UTF-8 fix; PYTHONUTF8=1 via set does not persist
- git commit -m with parens/dashes gets tokenized wrong by Desktop Commander — always use commit-msg.txt + git commit -F
- Emoji permanently banned — all icons must be cohesive inline SVG, stroke-based (see [icons-ban.md](http://icons-ban.md))
- Clearbit [logo.clearbit.com](http://logo.clearbit.com) blocked by DNS on host — use browser save or alternative source
- CSS CRITICAL: templates/styles.css and output/templates/styles.css are DIVERGED. Always edit output/templates/styles.css directly. Never copy from templates/styles.css — it will overwrite with stale rules. Use Desktop Commander:edit_block on output/templates/styles.css only.
- CSS CRITICAL: Multiple duplicate CSS rules in output/templates/styles.css from sprint history — run assets/find_dupes.py before adding new rules to check for conflicts.
- ✅ RESOLVED (DTS-BUG-01): `--clr-primary` alias added to :root in output/templates/styles.css → `--clr-primary: var(--accent-primary)`. Variable was not present in any current HTML (already clean), alias added as defensive CSS.
- ✅ RESOLVED (DTS-BUG-01): [activate-affiliate.py](http://activate-affiliate.py) Pattern 3 (legacy pending) updated to use order-independent attribute matching via lookaheads. Condition/insurance pages already converted to data-affiliate-status="direct" by PS-AFFILIATE-CTA-FIX-01 (handled by Patterns 1+2). affordable.html's 3 pending CTAs now matched by fixed Pattern 3. assets/prepare-condition-ctas.py added for ongoing audit.

## Page Inventory

### Reviews (34 live / 34 total) ✅ COMPLETE

- \[x\] betterhelp-review.html, talkspace-review.html, online-therapy-com-review.html
- \[x\] adhd-online-review.html, amwell-review.html, bend-health-review.html, brightline-review.html, brightside-review.html, calmerry-review.html, cerebral-review.html, circle-medical-review.html, doctor-on-demand-review.html, done-adhd-review.html
- \[x\] faithful-counseling-review.html, gay-therapy-center-review.html, grow-therapy-review.html, headspace-review.html, headway-review.html, inclusive-therapists-review.html, klarity-review.html, lunajoy-review.html, manatee-health-review.html, mindful-care-review.html
- \[x\] nocd-review.html, open-path-review.html, our-relationship-review.html, our-ritual-review.html, pride-counseling-review.html, psychology-today-review.html, regain-review.html, simplepractice-review.html, talkiatry-review.html, teen-counseling-review.html, therapyden-review.html

### Conditions (28 live / 28 total) ✅ COMPLETE

- \[x\] anxiety.html, depression.html, adhd.html, couples.html
- \[x\] ocd.html, ptsd.html, bipolar.html, eating-disorders.html
- \[x\] grief.html, anger.html, addiction.html, stress.html, burnout.html
- \[x\] relationship.html, lgbtq.html, teen.html, postpartum.html
- \[x\] insomnia.html, chronic-pain.html, social-anxiety.html
- \[x\] phobias.html, panic.html, loneliness.html, self-esteem.html
- \[x\] mens-mental-health.html, womens-mental-health.html
- \[x\] life-transitions.html, autism.html

### Insurance (23 live / 23 total) ✅ COMPLETE

- \[x\] aetna.html, bcbs.html, cigna.html, unitedhealthcare.html, medicaid.html, affordable.html
- \[x\] humana.html, kaiser.html, anthem.html, molina.html, oscar.html, ambetter.html
- \[x\] wellcare.html, tricare.html, chip.html, medicare.html, beacon.html
- \[x\] magellan.html, centene.html, highmark.html, harvard-pilgrim.html, tufts.html, community-health.html

### Hub Pages (3 live / 3 total) ✅ COMPLETE

- \[x\] reviews.html, conditions.html, insurance.html

### Supporting Pages (8 live)

- \[x\] index.html, about.html, editorial-policy.html, affiliate-disclosure.html
- \[x\] privacy-policy.html, crisis-resources.html, how-online-therapy-works.html, do-i-need-therapy.html

### SEO Files

- \[x\] output/sitemap.xml ✅
- \[x\] output/robots.txt ✅

## Launch Blockers

- \[x\] Domain — ✅ purchased and live ([digitaltherapysolutions.com](http://digitaltherapysolutions.com))
- \[x\] Editorial reviewer — ✅ DTS Research Team branding (Dr./LCSW/Licensed credentials scrubbed 2026-04-08)
- \[x\] Hero images — ✅ fixed 2026-04-08 (were missing from output/assets/)
- \[ \] Affiliate applications — in progress (see below)

## Affiliate Application Status (as of 2026-04-08)

Registry: assets/platform-registry.json — 32 programs with affiliate programs Activate: py assets/activate-affiliate.py --platform \[slug\] --url \[affiliate-url\]

### Network Status

- \[x\] Impact Radius — ✅ meta tag verified. Application submitted. Awaiting approval.
- \[ \] FlexOffers — DECLINED (new domain/no traffic). Reapply in 90 days with GSC data.
- \[ \] Commission Junction — not yet started

### GSC / Indexing Status

- \[x\] Google Search Console — ✅ property verified, sitemap submitted (2026-04-08)
- \[x\] Bing Webmaster Tools — ✅ verified + sitemap submitted 2026-04-23
- \[ \] Manual URL indexing requests — top priority pages (do via GSC URL Inspection)

### Applications In Progress

Priority 1 (direct programs, no traffic minimum):

- [Online-Therapy.com](http://Online-Therapy.com), Calmerry, Grow Therapy, Headway, Brightside, NOCD, Talkiatry, Klarity, Open Path Collective, Inclusive Therapists, ADHD Online, Circle Medical, Done, Lunajoy, Our Ritual, OurRelationship, TherapyDen, Gay Therapy Center

Priority 2 (network programs, may require traffic verification):

- BetterHelp (Impact Radius), Talkspace (CJ), ReGain (IR), Teen Counseling (IR), Pride Counseling (IR), Faithful Counseling (IR), Cerebral (direct), Amwell (CJ), Headspace (IR), Doctor on Demand (CJ), Brightline, Bend Health, Manatee, Mindful Care

### W-9 Notes

- Entity: Borrowed Light Group LLC
- Box 2: Borrowed Light Group LLC | Box 3: LLC → D (disregarded) | Part I: BLG EIN
- E-sign acceptable, no wet ink required
