Execute Sprint PS-PLATFORMS-01 — All 31 Platform Review Pages for Digital Therapy Solutions.
Run after PS-DESIGN-QA-02 ✅ complete.

Read these files FIRST before doing anything:
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\STATUS.md
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\betterhelp-review.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\talkspace-review.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\reviews.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\templates\styles.css

Summary: After this sprint, all 34 platform review pages will exist. The 31 new pages
follow the exact betterhelp-review.html structure. All CTA buttons use
data-affiliate-status="pending" with href="#" — a single patch script activates them
per platform when contracts are signed. The reviews.html hub will show all 34 cards
as live-linked. The site is fully built and affiliate-ready.

---

TOGGLE ARCHITECTURE — read this before writing a single page

Every CTA button on every new page uses this pattern:

  <a href="#" class="cta-button cta-button--pending" data-affiliate-status="pending"
     data-platform="[slug]">
    Coming Soon — Check Back
  </a>

When a contract is signed for a platform, run assets/activate-affiliate.py with the
slug and URL to flip that platform's CTA live across the page:
  python assets/activate-affiliate.py --platform betterhelp --url https://betterhelp.com/aff/...
That script: finds all data-platform="[slug]" CTAs, sets href to the affiliate URL,
removes cta-button--pending class, updates button text to "Visit [Platform] →".

Write assets/activate-affiliate.py as Task 1 BEFORE building any pages.
Also add to styles.css:
  .cta-button--pending { opacity: 0.5; cursor: not-allowed; background: var(--text-muted); }

The 3 existing review pages (betterhelp, talkspace, online-therapy-com) should also
be retrofitted with data-affiliate-status="pending" on their CTA buttons in this sprint.

---

TASK 1 — Write assets/activate-affiliate.py

Script usage: python assets/activate-affiliate.py --platform [slug] --url [affiliate_url]
- Reads target output/[slug]-review.html
- Finds all <a> tags with data-platform="[slug]"
- Sets href to affiliate_url
- Removes class cta-button--pending
- Updates button text to "Visit [Platform Name] →"
- Writes file back
- Prints: "Activated [slug] → [url]"
sys.stdout.reconfigure(encoding='utf-8'). Write to file before running.

Also retrofit existing 3 review pages:
- output/betterhelp-review.html — find CTA buttons, add data-platform="betterhelp" data-affiliate-status="pending" class="cta-button cta-button--pending"
- output/talkspace-review.html — same, data-platform="talkspace"
- output/online-therapy-com-review.html — same, data-platform="online-therapy-com"

Add .cta-button--pending CSS to templates/styles.css.

---

TASK 2 — Update reviews.html — activate all 34 hub cards

Currently 31 cards on reviews.html are hub-card--stub (greyed, no link).
Update all 31 stub cards to live cards pointing to their review page.
Stub card pattern to replace for each platform:
  Remove hub-card--stub class
  Change CTA from "Coming Soon" to "Read Review →"
  Add href="[slug]-review.html" to the card anchor

Write assets/activate-review-hub.py to do this in one pass — map all 31 slugs to their
hub card. Write to file, run from D:\Work\Digital-Therapy-Solutions.


---

TASK 3 — Build all 31 platform review pages

Files to create (all in output/):
adhd-online-review.html, amwell-review.html, bend-health-review.html,
brightline-review.html, brightside-review.html, calmerry-review.html,
cerebral-review.html, circle-medical-review.html, doctor-on-demand-review.html,
done-adhd-review.html, faithful-counseling-review.html, gay-therapy-center-review.html,
grow-therapy-review.html, headspace-review.html, headway-review.html,
inclusive-therapists-review.html, klarity-review.html, lunajoy-review.html,
manatee-health-review.html, mindful-care-review.html, nocd-review.html,
open-path-review.html, our-relationship-review.html, our-ritual-review.html,
pride-counseling-review.html, psychology-today-review.html, regain-review.html,
simplepractice-review.html, talkiatry-review.html, teen-counseling-review.html,
therapyden-review.html

STRUCTURE: Every page must exactly match betterhelp-review.html structure:
- Full HTML head: charset, viewport, title, meta description, favicon, fonts, stylesheet
- Canonical: <link rel="canonical" href="https://digitaltherapysolutions.com/[slug]-review">
- BreadcrumbList JSON-LD: Home > Reviews > [Platform] Review
- Review JSON-LD: Schema.org Review with ratingValue, reviewBody
- Nav: identical to betterhelp-review.html (5 links, hamburger, brand)
- Breadcrumb nav: Home / Reviews / [Platform Name] Review
- Hero: hero-visual (hero.webp) + hero-text with h1, 2 subheads, trust-row
- Section divider SVG
- Verdict box section (section-wrapper--alt)
- Platform details card with logo, score, verdict-box, body paragraph, details pills, CTA
- Pricing section (split-section pattern)
- Who it's best for (feature-list with checkmark SVGs)
- Who should look elsewhere (feature-list with minus SVGs)
- Session formats section (split-section)
- Pull quote (1 per page)
- Comparison forks section (links to related reviews + conditions)
- Footer (identical to betterhelp-review.html)
- No inline <style> blocks
- Asset paths: ../assets/

CTA PATTERN ON EVERY PAGE (mandatory):
  <a href="#" class="cta-button cta-button--pending" data-affiliate-status="pending"
     data-platform="[slug]">Coming Soon — Check Back</a>

PLATFORM DATA — use this for each page:

ADHD Online | adhd-online | #1976D2 | AO | Score: 4.0
  Best for: ADHD-specific telehealth — diagnosis + therapy + medication management
  Pricing: $199-299/month | Insurance: Some plans accepted | Formats: Video
  Verdict: Specialized ADHD platform covering evaluation, therapy, and medication in one place. Best for adults seeking diagnosis or ongoing medication management online.
  Best for: Adults seeking ADHD diagnosis, ongoing medication management, combined therapy+psychiatry
  Look elsewhere: If you want broad therapy topics beyond ADHD, or need sliding scale pricing

Amwell | amwell | #0277BD | AW | Score: 3.8
  Best for: Insurance-covered urgent mental health — large telehealth network
  Pricing: $109-279/session | Insurance: Most major plans | Formats: Video
  Verdict: Amwell is a broad telehealth network, not a therapy-first platform. Useful for insured patients who want mental health covered under existing telehealth benefits.
  Best for: People with insurance who want therapy integrated into general telehealth, one-off sessions
  Look elsewhere: If you want ongoing weekly therapy with a dedicated therapist

Bend Health | bend-health | #43A047 | BH | Score: 4.1
  Best for: Kids and teens — whole-family mental health coaching and therapy
  Pricing: $195-295/month | Insurance: Several plans | Formats: Video
  Verdict: Bend Health focuses on pediatric and adolescent mental health with a coaching + therapy model. One of the few platforms designed for the whole family.
  Best for: Parents seeking mental health support for children 2-17, family-involved care
  Look elsewhere: If you need adult individual therapy

Brightline | brightline | #FF7043 | BL | Score: 4.2
  Best for: Children and teens — behavioral health coaching + therapy
  Pricing: $195/month+ | Insurance: Major plans including BCBS | Formats: Video
  Verdict: Brightline specializes in pediatric behavioral health. Strong coaching model for kids with anxiety, ADHD, or behavioral challenges. Employer-sponsored plans widely available.
  Best for: Children 1-17 with behavioral or emotional challenges, employer-insured families
  Look elsewhere: Adults, or anyone without Brightline-covered insurance

Brightside | brightside | #5C6BC0 | BS | Score: 4.3
  Best for: Anxiety and depression with medication — integrated therapy + psychiatry
  Pricing: $95-349/month | Insurance: Most major plans | Formats: Video
  Verdict: Brightside treats anxiety and depression with therapy and medication management together. One of the cleaner integrated care models — no separate referrals needed.
  Best for: People with anxiety or depression who may benefit from both therapy and medication
  Look elsewhere: If you need specialized therapy (trauma, OCD, couples) — Brightside is condition-specific

Calmerry | calmerry | #26A69A | CM | Score: 4.2
  Best for: Budget-conscious therapy — transparent pricing, no hidden fees
  Pricing: $42-70/week | Insurance: Not accepted | Formats: Video + Chat + Messaging
  Verdict: Calmerry competes on pricing transparency. What you see is what you pay, with CBT-based tools included. Smaller therapist network than BetterHelp but honest pricing.
  Best for: People paying out of pocket who want predictable costs and async messaging
  Look elsewhere: If you need insurance coverage or psychiatry

Cerebral | cerebral | #7B1FA2 | Ce | Score: 3.7
  Best for: Medication management — psychiatry-first platform with therapy add-on
  Pricing: $85-325/month | Insurance: Several plans | Formats: Video + Messaging
  Verdict: Cerebral has had a troubled history with regulatory scrutiny around stimulant prescribing. They've restructured but the reputation hit is real. Solid for non-controlled medication management.
  Best for: Adults needing psychiatric medication management (non-stimulants), insured patients
  Look elsewhere: If you have concerns about platform history, or specifically need ADHD stimulant management


Circle Medical | circle-medical | #00ACC1 | CM | Score: 3.9
  Best for: Primary care + mental health — integrated medical telehealth
  Pricing: Insurance-based ($20-50 copay) | Insurance: Most plans | Formats: Video
  Verdict: Circle Medical is a primary care telehealth platform with mental health as one service. Good if you want one provider relationship for both physical and mental health. Not a therapy-depth platform.
  Best for: People who want mental health integrated with general primary care, insured patients
  Look elsewhere: Deep therapy work, specialized conditions, or if you want a dedicated therapist

Doctor on Demand | doctor-on-demand | #1565C0 | DD | Score: 3.8
  Best for: Insurance-covered urgent mental health — established telehealth brand
  Pricing: $179-299/session self-pay | Insurance: Most major plans | Formats: Video
  Verdict: Doctor on Demand is a legacy telehealth platform with solid insurance coverage. Better for psychiatric evaluation and urgent needs than ongoing weekly therapy.
  Best for: Insured patients, psychiatric evaluation, one-off urgent mental health appointments
  Look elsewhere: Ongoing dedicated therapy, budget self-pay options

Done ADHD | done-adhd | #F57C00 | DA | Score: 4.0
  Best for: ADHD diagnosis and medication — streamlined online evaluation
  Pricing: $199 evaluation + $79/month | Insurance: Limited | Formats: Video + Async
  Verdict: Done focuses narrowly on ADHD evaluation and medication management. Fast, relatively affordable pathway to an ADHD diagnosis and stimulant prescription online.
  Best for: Adults who suspect ADHD and want evaluation + ongoing medication management
  Look elsewhere: If you want therapy alongside medication, or need insurance coverage

Faithful Counseling | faithful-counseling | #5D4037 | FC | Score: 4.0
  Best for: Christian therapy — faith-integrated counseling online
  Pricing: $65-100/week | Insurance: Not accepted | Formats: Video + Phone + Messaging
  Verdict: Faithful Counseling (by BetterHelp) connects users with Christian therapists who integrate faith into sessions. Same platform infrastructure as BetterHelp, faith-filtered therapist pool.
  Best for: Christians who want a therapist who shares their faith and integrates it into treatment
  Look elsewhere: If faith integration isn't important to you — BetterHelp gives you the same platform at the same price with more therapist options

Gay Therapy Center | gay-therapy-center | #E91E63 | GT | Score: 4.2
  Best for: LGBTQ+ affirming therapy — vetted queer and trans-competent therapists
  Pricing: $150-250/session | Insurance: Limited | Formats: Video + In-person (select)
  Verdict: Gay Therapy Center is a directory-style platform connecting LGBTQ+ clients with vetted affirming therapists. Not a subscription model — you book directly with therapists.
  Best for: LGBTQ+ individuals who prioritize therapist identity affirmation and vetting
  Look elsewhere: If you need insurance coverage or a subscription pricing model

Grow Therapy | grow-therapy | #2E7D32 | GT | Score: 4.3
  Best for: Insurance + therapist choice — browse profiles before booking
  Pricing: Insurance-based | Insurance: Most major plans | Formats: Video + In-person
  Verdict: Grow Therapy lets you browse real therapist profiles and book directly — no algorithm matching. One of the best options for insured clients who want control over who they see.
  Best for: Insured clients who want to choose their own therapist by specialty and profile
  Look elsewhere: If you don't have insurance or want a subscription/messaging model

Headspace | headspace | #FF6D00 | Hs | Score: 3.5
  Best for: Mindfulness and mental wellness — not traditional therapy
  Pricing: $12.99-69.99/month | Insurance: Some employer plans | Formats: App + Guided content
  Verdict: Headspace is a mental wellness app, not a therapy platform. Meditation, sleep content, and guided exercises. Valuable as a supplement to therapy, not a replacement.
  Best for: People managing mild stress or building mindfulness habits alongside other support
  Look elsewhere: Anyone who needs actual therapy — Headspace is not a substitute

Headway | headway | #6200EA | Hw | Score: 4.4
  Best for: Insurance + therapist choice — largest insurance-accepting directory
  Pricing: Insurance-based ($0-50 copay typically) | Insurance: Most major plans | Formats: Video + In-person
  Verdict: Headway is a therapist network that handles insurance billing on behalf of independent therapists. One of the best platforms for finding an in-network therapist across most major insurers.
  Best for: Insured clients who want the widest selection of in-network therapists
  Look elsewhere: If you don't have insurance, or want a subscription with messaging


Inclusive Therapists | inclusive-therapists | #7B1FA2 | IT | Score: 4.2
  Best for: Marginalized identities — LGBTQ+, BIPOC, disability-affirming therapist directory
  Pricing: Varies by therapist ($80-200/session, sliding scale available) | Insurance: Varies | Formats: Video + In-person
  Verdict: Inclusive Therapists is a directory specifically built for people seeking culturally responsive, identity-affirming therapists. Browse by identity, filter by specialty, connect directly.
  Best for: LGBTQ+, BIPOC, disabled, or neurodivergent people seeking affirming therapists
  Look elsewhere: If you want a subscription model or messaging-based therapy

Klarity | klarity | #00BCD4 | Kl | Score: 3.9
  Best for: Psychiatric medication — online prescriptions for ADHD, anxiety, depression
  Pricing: $149-199/month | Insurance: Limited | Formats: Video
  Verdict: Klarity connects patients with psychiatric providers for medication management. Fast access to prescriptions for common conditions. Not a therapy platform — medication only.
  Best for: Adults seeking psychiatric medication management without a lengthy waitlist
  Look elsewhere: If you need therapy alongside medication, or want insurance coverage

LunaJoy | lunajoy | #AD1457 | LJ | Score: 4.1
  Best for: Women's mental health — perinatal, postpartum, hormonal mental health focus
  Pricing: Insurance-based | Insurance: Several plans | Formats: Video
  Verdict: LunaJoy specializes in women's mental health across life stages — pregnancy, postpartum, perimenopause, and hormonal transitions. Therapists and psychiatrists on one platform.
  Best for: Women seeking care specifically attuned to hormonal mental health, postpartum depression
  Look elsewhere: General therapy needs, men, non-hormone-related conditions

Manatee Health | manatee-health | #006064 | MH | Score: 4.0
  Best for: Child and teen therapy — parent-involved online therapy model
  Pricing: $150-200/session | Insurance: Several plans | Formats: Video
  Verdict: Manatee's model involves parents in their child's therapy process, providing coaching and tools alongside the therapist. Designed for kids 5-17 with behavioral or emotional challenges.
  Best for: Parents of children with anxiety, ADHD, OCD, or behavioral challenges
  Look elsewhere: Adults, or families wanting child-only sessions without parent involvement

Mindful Care | mindful-care | #1B5E20 | MC | Score: 3.9
  Best for: Insurance-based psychiatric care — medication management in New York and nearby states
  Pricing: Insurance-based | Insurance: Most major plans in NY/NJ/IL/TX | Formats: Video + In-person
  Verdict: Mindful Care is a regionally focused psychiatric and therapy practice with telehealth access. Strong insurance coverage but limited to specific states.
  Best for: Insured patients in NY, NJ, IL, TX seeking psychiatric care
  Look elsewhere: If you're outside their service states, or need nationwide coverage

NOCD | nocd | #1A237E | NC | Score: 4.5
  Best for: OCD — the most specialized online OCD therapy platform available
  Pricing: Insurance-based ($20-100 copay) + $149/month self-pay | Insurance: Most major plans | Formats: Video + Async
  Verdict: NOCD is built specifically for OCD with ERP-trained therapists, between-session support, and peer community. The best online option for OCD by a significant margin.
  Best for: Anyone with OCD seeking ERP therapy — the gold standard treatment
  Look elsewhere: If you don't have OCD — NOCD is narrow by design

Open Path | open-path | #2E7D32 | OP | Score: 4.4
  Best for: Affordable in-network therapy — sliding scale $30-80/session
  Pricing: $30-80/session (one-time $65 membership) | Insurance: Not accepted | Formats: Video + In-person
  Verdict: Open Path is the best option for uninsured or underinsured clients who want real therapy at accessible prices. Therapists set their own sliding scale rates. One-time membership fee.
  Best for: Uninsured or underinsured adults who want affordable weekly sessions
  Look elsewhere: If you have insurance — Headway or Grow Therapy will be cheaper with coverage

Our Relationship | our-relationship | #C62828 | OR | Score: 4.1
  Best for: Couples — structured online relationship program (not live therapist sessions)
  Pricing: $149 one-time | Insurance: Not accepted | Formats: Self-guided program
  Verdict: Our Relationship is a research-backed self-guided couples program, not ongoing live therapy. Developed at University of Chicago. Strong evidence base for relationship satisfaction.
  Best for: Couples wanting a structured, affordable program to improve communication
  Look elsewhere: If you need live couples therapy — this is a program, not a therapist match

Our Ritual | our-ritual | #880E4F | Ri | Score: 3.9
  Best for: Relationship coaching — hybrid coaching and therapy for couples
  Pricing: $95-195/month | Insurance: Not accepted | Formats: Video + App tools
  Verdict: Our Ritual combines relationship coaching with app-based tools and exercises. Somewhere between self-help and couples therapy. Better for prevention and growth than acute crisis.
  Best for: Couples wanting ongoing relationship maintenance and communication tools
  Look elsewhere: If you're in relationship crisis — you need a licensed couples therapist

Pride Counseling | pride-counseling | #9C27B0 | PC | Score: 4.0
  Best for: LGBTQ+ therapy — BetterHelp's LGBTQ+ focused platform
  Pricing: $65-100/week | Insurance: Not accepted | Formats: Video + Phone + Messaging
  Verdict: Pride Counseling (by BetterHelp) filters the BetterHelp therapist pool for LGBTQ+ affirming providers. Same infrastructure, same pricing, LGBTQ+-forward matching.
  Best for: LGBTQ+ individuals who want affirming therapy without vetting therapists themselves
  Look elsewhere: If insurance coverage matters — BetterHelp platforms don't accept insurance

Psychology Today | psychology-today | #00796B | PT | Score: 4.0
  Best for: Finding a therapist — the largest therapist directory in the US
  Pricing: Varies by therapist ($80-300/session) | Insurance: Varies by therapist | Formats: Video + In-person
  Verdict: Psychology Today is a directory, not a platform. No integrated booking, billing, or messaging — you contact therapists directly. Unmatched for finding local or specialized therapists.
  Best for: Finding a therapist by specialty, location, insurance, or approach — maximum control
  Look elsewhere: If you want integrated booking, billing, and sessions in one app

Regain | regain | #C0392B | Re | Score: 4.1
  Best for: Couples therapy online — BetterHelp's couples platform
  Pricing: $65-100/week | Insurance: Not accepted | Formats: Video + Phone + Messaging
  Verdict: Regain (by BetterHelp) is built for couples, with matching to therapists who specialize in relationship counseling. Same BetterHelp infrastructure, couples-focused filtering.
  Best for: Couples who want online therapy without insurance and want fast matching
  Look elsewhere: If you need insurance coverage — Grow Therapy has in-network couples therapists

SimplePractice | simplepractice | #4A90D9 | SP | Score: 3.7
  Best for: Finding a therapist who uses SimplePractice — not a consumer platform
  Pricing: Varies by therapist | Insurance: Varies | Formats: Video + In-person
  Verdict: SimplePractice is practice management software for therapists. The client-facing portal lets patients book and attend sessions with their existing SimplePractice-using therapist. Not a marketplace.
  Best for: Existing patients whose therapist uses SimplePractice for scheduling and video
  Look elsewhere: If you're looking to find a new therapist — use Headway, Psychology Today, or Grow Therapy instead

Talkiatry | talkiatry | #283593 | Ta | Score: 4.3
  Best for: Psychiatry with insurance — in-network psychiatric care, medication + therapy
  Pricing: Insurance-based ($30-100 copay) | Insurance: Most major plans | Formats: Video
  Verdict: Talkiatry is a psychiatric practice that accepts insurance and offers both medication management and therapy. One of the most insurance-friendly psychiatric platforms.
  Best for: Insured adults seeking psychiatric evaluation, medication, and/or ongoing therapy
  Look elsewhere: If you don't need psychiatry — a therapy-only platform will be more cost-effective

Teen Counseling | teen-counseling | #00695C | TC | Score: 4.1
  Best for: Teenagers — BetterHelp's teen-specific therapy platform
  Pricing: $65-100/week | Insurance: Not accepted | Formats: Video + Phone + Messaging
  Verdict: Teen Counseling (by BetterHelp) matches teenagers 13-19 with therapists who specialize in adolescent issues. Parents can be involved at the teen's discretion. Same BetterHelp infrastructure.
  Best for: Teenagers needing therapy, parents seeking mental health support for their teen
  Look elsewhere: If insurance coverage is needed — Teen Counseling doesn't accept insurance

TherapyDen | therapyden | #2E7D32 | TD | Score: 4.1
  Best for: Finding therapists by specialty and identity — values-forward directory
  Pricing: Varies by therapist (sliding scale common) | Insurance: Varies | Formats: Video + In-person
  Verdict: TherapyDen is a therapist directory that emphasizes sliding scale access and identity-affirming care. Strong filtering for LGBTQ+, BIPOC, neurodivergent, and other communities.
  Best for: People who want to filter by therapist values, identity, sliding scale availability
  Look elsewhere: If you want integrated platform features — TherapyDen is a directory only


---

TASK 4 — Update sitemap.xml

After all 31 pages are built, regenerate output/sitemap.xml to include the new pages.
Run: python assets/generate_sitemap.py (already exists from PS-SEO-01).
All new review pages get priority 0.8 and changefreq "monthly".

---

<!-- phase:execute -->

TASK 5 — Quality gate + session close

1. Run D:\Work\Digital-Therapy-Solutions\quality_gate.py — 0 failures.
   Page count: 97 (66 existing + 31 new).
2. Verify 3 pages in browser spot-check:
   - nocd-review.html: correct structure, pending CTA visible
   - grow-therapy-review.html: correct structure, pending CTA visible
   - reviews.html: all 34 cards live-linked, none greyed
3. Friction pass — FIX NOW / BACKLOG / LOG ONLY. Present before proceeding.
4. Write MORNING_BRIEFING.md to D:\Work\Digital-Therapy-Solutions\MORNING_BRIEFING.md
5. Update STATUS.md:
   - Mark PS-PLATFORMS-01 ✅ COMPLETE with commit hash
   - Update Reviews: 34 live / 34 total ✅ COMPLETE
   - Add note: activate-affiliate.py ready for use when contracts signed
6. Write commit to D:\Work\Digital-Therapy-Solutions\commit-msg.txt:
   feat(platforms): PS-PLATFORMS-01 — 31 review pages, pending CTAs, affiliate toggle system
7. git add . && git commit -F commit-msg.txt && git push

---

CRITICAL CONSTRAINTS:
- No emoji anywhere — icons-ban.md policy active
- No inline <style> blocks — all CSS in templates/styles.css
- Asset paths: ../assets/ (output pages are one level deep)
- Stylesheet: ../templates/styles.css
- Every CTA uses data-affiliate-status="pending" href="#" class="cta-button cta-button--pending"
- Write Python scripts to file before running (cmd 500 char limit)
- sys.stdout.reconfigure(encoding='utf-8') in every script
- git commit always via commit-msg.txt + git commit -F
- Build pages in batches of 4-5 — do not attempt all 31 in one pass
- Read betterhelp-review.html before building each batch to stay pattern-locked

ACCEPTANCE CRITERIA:
- [ ] assets/activate-affiliate.py exists and documented
- [ ] .cta-button--pending CSS added to styles.css
- [ ] 3 existing review pages retrofitted with data-affiliate-status="pending"
- [ ] 31 new review pages exist in output/, all following betterhelp-review.html structure
- [ ] All 31 pages have pending CTA with data-platform="[slug]"
- [ ] All 31 pages have BreadcrumbList + Review JSON-LD
- [ ] reviews.html — all 34 cards live-linked, 0 stubs
- [ ] output/sitemap.xml regenerated with 97 pages
- [ ] quality_gate.py — 0 failures, 97 pages
- [ ] STATUS.md updated, Reviews 34/34 ✅
- [ ] MORNING_BRIEFING.md written before commit
- [ ] Committed and pushed — Vercel auto-deploy triggered
