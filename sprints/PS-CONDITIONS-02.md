Execute Sprint PS-CONDITIONS-02 — 4 Remaining Condition Pages for Digital Therapy Solutions.
Run after PS-CONDITIONS-01 ✅ and PS-DESIGN-QA-01 ✅ complete.

Read these files FIRST before doing anything:
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\STATUS.md
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\ocd.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\conditions.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\output\index.html
  Filesystem:read_file D:\Work\Digital-Therapy-Solutions\templates\styles.css

Summary: After this sprint, all 28 condition pages will be live and all 28 cards on
conditions.html will be fully linked. The 4 stub cards (Men's Mental Health, Women's
Mental Health, Life Transitions, Autism & Neurodivergence) will become real pages
following the exact pattern of PS-CONDITIONS-01. The conditions vertical will be 100%
complete.

Tasks:

1. Audit conditions.html — locate the 4 stub cards:
   Identify the exact HTML for the 4 stub entries currently on conditions.html:
   Men's Mental Health, Women's Mental Health, Life Transitions, Autism & Neurodivergence.
   Note their current href values, icon SVGs (or lack thereof), and stub class names.
   These will be updated in Task 5 once pages are built.

2. Build output/mens-mental-health.html:
   Follow ocd.html EXACTLY for all structural elements — DOCTYPE, head, fonts, favicon,
   stylesheet path (../templates/styles.css), nav, breadcrumb, hero, section divider,
   platform cards, forks section, footer.

   Breadcrumb: Home > Conditions > Men's Mental Health
   Hero h1: "Men's mental health doesn't get talked about enough. These platforms get it."
   Hero subhead italic: <em>"Stoicism isn't a treatment plan. Therapists who understand that make all the difference."</em>
   Hero subhead follow: "We reviewed platforms specifically for how well they serve men seeking therapy."
   Trust row: 34+ Platforms Reviewed | Expert-Written | Updated Monthly | No Sponsored Rankings

   Platform cards (3):
   Card 1 — BetterHelp (featured, Top Rated, 4.5/5)
     Logo: ../assets/logos/betterhelp.webp | Color: #00796B | Initial: BH
     Tagline: Best overall for men — massive therapist network, easy to switch
     Body: BetterHelp's size works in its favor here. With 30,000+ therapists, men can
     specifically request someone who works with male clients on traditional masculine
     norms, identity, or career stress — and actually find a match. The platform doesn't
     market specifically to men, but the depth of the network means the right therapist
     exists. Cost is $65–100/week without insurance.
     Details: $65–100/week | No insurance required | Video + Phone + Messaging
     CTA offer: ✦ Specify your therapist preferences at signup
     CTA button: Find a Therapist on BetterHelp

   Card 2 — Talkspace (Recommended, 4.3/5)
     Logo: ../assets/logos/talkspace.webp | Color: #009688 | Initial: TS
     Tagline: Best if you have insurance — in-network with most major plans
     Body: If cost is the barrier keeping men from therapy, Talkspace removes it for
     insured clients. In-network with Aetna, Cigna, and others, bringing sessions down
     to $10–50 copay range. The async messaging format also appeals to men who prefer
     to process in writing before speaking. Psychiatry available if medication is part
     of the picture.
     Details: $10–50/session w/ insurance | $69–109/week self-pay | Video + Messaging
     CTA offer: ✦ Check your insurance coverage at signup
     CTA button: Check Coverage on Talkspace

   Card 3 — Grow Therapy (Recommended, 4.2/5)
     Logo: ../assets/logos/grow-therapy.webp | Color: #2E7D32 | Initial: GT
     Tagline: Best for insurance + therapist choice — browse real profiles before booking
     Body: Grow Therapy lets you browse actual therapist profiles, read bios, and see
     specialties before committing — which matters when you're looking for someone who
     specifically works with men on anger, identity, or relationship issues. In-network
     with most major insurers. You book directly, no algorithm matching.
     Details: Varies by insurance | Self-pay $100–200/session | Video + In-person options
     CTA offer: ✦ Browse therapist profiles — no commitment to book
     CTA button: Browse Therapists on Grow Therapy

   Forks section (below cards):
     Heading: <em>Also worth reading</em>
     Links: Online therapy for stress → stress.html | Online therapy for anger → anger.html |
     Online therapy for addiction → addiction.html | All conditions → conditions.html


3. Build output/womens-mental-health.html:
   Same structural pattern as ocd.html exactly.

   Breadcrumb: Home > Conditions > Women's Mental Health
   Hero h1: "Women carry a lot. Therapy built around that reality helps more."
   Hero subhead italic: <em>"Hormones, relationships, caregiving, identity — the full picture matters in treatment."</em>
   Hero subhead follow: "These platforms have the therapist depth to match women with someone who actually understands."
   Trust row: 34+ Platforms Reviewed | Expert-Written | Updated Monthly | No Sponsored Rankings

   Platform cards (3):
   Card 1 — BetterHelp (featured, Top Rated, 4.6/5)
     Logo: ../assets/logos/betterhelp.webp | Color: #00796B | Initial: BH
     Tagline: Best overall for women — largest network, easy to find female therapists
     Body: Women can specifically request a female therapist on BetterHelp — and with
     30,000+ licensed professionals on the platform, that request actually gets fulfilled.
     Therapists who specialize in postpartum, hormonal transitions, relationship trauma,
     and burnout are well represented. Cost runs $65–100/week; financial aid available.
     Details: $65–100/week | Financial aid available | Video + Phone + Messaging
     CTA offer: ✦ Request a female therapist at signup — it's a standard option
     CTA button: Find a Therapist on BetterHelp

   Card 2 — Talkspace (Recommended, 4.4/5)
     Logo: ../assets/logos/talkspace.webp | Color: #009688 | Initial: TS
     Tagline: Best with insurance — strong coverage for women's mental health care
     Body: Talkspace covers therapy and psychiatry under most major insurance plans —
     useful for women managing postpartum depression, anxiety tied to hormonal shifts,
     or conditions that benefit from both talk therapy and medication management.
     Messaging format suits women who process better in writing. $10–50 copay range
     with insurance.
     Details: $10–50/session w/ insurance | $69–109/week self-pay | Video + Messaging + Psychiatry
     CTA offer: ✦ Therapy and psychiatry in one platform — useful for hormonal conditions
     CTA button: Check Coverage on Talkspace

   Card 3 — Brightside (Recommended, 4.3/5)
     Logo: ../assets/logos/brightside.webp | Color: #5C6BC0 | Initial: BS
     Tagline: Best for anxiety + depression with medication — integrated care model
     Body: Brightside treats anxiety and depression with both therapy and medication
     management on one platform — a practical option for women where hormonal changes
     intersect with mood disorders. Psychiatry appointments available within days.
     Accepts most major insurance. $95–349/month depending on plan.
     Details: $95–349/month | Insurance accepted | Therapy + Psychiatry integrated
     CTA offer: ✦ Therapy and medication managed together — no separate referrals
     CTA button: Get Started on Brightside

   Forks section:
     Heading: <em>Also worth reading</em>
     Links: Online therapy for postpartum → postpartum.html | Online therapy for anxiety → anxiety.html |
     Online therapy for eating disorders → eating-disorders.html | All conditions → conditions.html

4. Build output/life-transitions.html:
   Same structural pattern as ocd.html exactly.

   Breadcrumb: Home > Conditions > Life Transitions
   Hero h1: "Big changes don't come with instructions. Therapy helps you write them."
   Hero subhead italic: <em>"Divorce, job loss, relocation, retirement, loss — transitions hit differently when you're carrying them alone."</em>
   Hero subhead follow: "These platforms have therapists who specialize in adjustment, grief, and finding footing again."
   Trust row: 34+ Platforms Reviewed | Expert-Written | Updated Monthly | No Sponsored Rankings

   Platform cards (3):
   Card 1 — BetterHelp (featured, Top Rated, 4.5/5)
     Logo: ../assets/logos/betterhelp.webp | Color: #00796B | Initial: BH
     Tagline: Best for transitions — therapist specialties include adjustment and life change
     Body: Life transitions often don't fit a clinical diagnosis — which creates problems
     for insurance coverage but not for BetterHelp. Their self-pay model means you don't
     need a diagnosis code to get matched with someone who works specifically with career
     change, divorce, relocation, or loss. Switching therapists is easy if the first match
     isn't right. $65–100/week.
     Details: $65–100/week | No diagnosis required | Video + Phone + Messaging
     CTA offer: ✦ No diagnosis needed — adjustment and transition are enough
     CTA button: Find a Therapist on BetterHelp

   Card 2 — Grow Therapy (Recommended, 4.2/5)
     Logo: ../assets/logos/grow-therapy.webp | Color: #2E7D32 | Initial: GT
     Tagline: Best with insurance — browse therapists by specialty before booking
     Body: Grow Therapy lets you filter by specialty — you can specifically search for
     therapists who work with grief, adjustment disorder, or life transitions. Profiles
     include bios and specialties so you know what you're getting before the first
     session. In-network with most major plans.
     Details: Insurance-based pricing | $100–200/session self-pay | Video + In-person
     CTA offer: ✦ Filter by "life transitions" in therapist search
     CTA button: Browse Therapists on Grow Therapy

   Card 3 — Online-Therapy.com (Recommended, 4.1/5)
     Logo: ../assets/logos/online-therapy.webp | Color: #4CAF50 | Initial: OT
     Tagline: Best structured program — CBT-based tools alongside live sessions
     Body: Online-Therapy.com pairs weekly sessions with CBT worksheets and journaling
     tools — useful during transitions where you want structured support between sessions,
     not just talk. The $45–80/week pricing makes consistent weekly therapy accessible
     even without insurance.
     Details: $45–80/week | No insurance required | Video + CBT worksheets + Journaling
     CTA offer: ✦ CBT tools between sessions — structure during uncertain times
     CTA button: Get Started on Online-Therapy.com

   Forks section:
     Heading: <em>Also worth reading</em>
     Links: Online therapy for grief → grief.html | Online therapy for stress → stress.html |
     Online therapy for burnout → burnout.html | All conditions → conditions.html


5. Build output/autism.html:
   Same structural pattern as ocd.html exactly.

   Breadcrumb: Home > Conditions > Autism & Neurodivergence
   Hero h1: "Therapy for autistic adults should be affirming, not corrective."
   Hero subhead italic: <em>"The right therapist understands how you process — and works with it, not against it."</em>
   Hero subhead follow: "These platforms have therapists with neurodiversity-affirming training and real experience with autistic adults."
   Trust row: 34+ Platforms Reviewed | Expert-Written | Updated Monthly | No Sponsored Rankings

   Platform cards (3):
   Card 1 — Grow Therapy (featured, Top Rated, 4.4/5)
     Logo: ../assets/logos/grow-therapy.webp | Color: #2E7D32 | Initial: GT
     Tagline: Best for finding neurodiversity-affirming therapists — searchable by specialty
     Body: Grow Therapy's profile-browse model is the right fit here — you can search
     specifically for therapists with autism or neurodivergence experience, read their
     bios, and verify their approach before booking. For autistic adults, therapist fit
     matters more than platform features. Insurance-based pricing brings the cost down
     significantly for most plans.
     Details: Insurance-based pricing | $100–200/session self-pay | Video + In-person options
     CTA offer: ✦ Search "autism" or "neurodivergence" in therapist specialty filter
     CTA button: Browse Therapists on Grow Therapy

   Card 2 — BetterHelp (Recommended, 4.3/5)
     Logo: ../assets/logos/betterhelp.webp | Color: #00796B | Initial: BH
     Tagline: Best for access and flexibility — async messaging suits many autistic clients
     Body: BetterHelp's messaging format works well for autistic clients who prefer
     written communication, need more processing time, or find video sessions draining.
     The platform lets you specify therapist preferences including neurodivergence
     experience. The large network means you can switch if the first match isn't right.
     $65–100/week; financial aid available.
     Details: $65–100/week | Financial aid available | Video + Phone + Messaging (async)
     CTA offer: ✦ Async messaging option — communicate on your own schedule
     CTA button: Find a Therapist on BetterHelp

   Card 3 — Inclusive Therapists (Recommended, 4.2/5)
     Logo: ../assets/logos/inclusive-therapists.webp | Color: #7B1FA2 | Initial: IT
     Tagline: Best directory for marginalized identities — neurodivergent-affirming focus
     Body: Inclusive Therapists is a directory specifically built for people seeking
     therapists who affirm their identity — including neurodivergent and autistic clients.
     You browse profiles, filter by neurodiversity affirmation, and connect directly.
     Pricing varies by therapist; many offer sliding scale rates.
     Details: Varies by therapist | Sliding scale available | Video + In-person
     CTA offer: ✦ Filter by neurodivergent-affirming in the therapist search
     CTA button: Browse Therapists on Inclusive Therapists

   Forks section:
     Heading: <em>Also worth reading</em>
     Links: Online therapy for ADHD → adhd.html | Online therapy for anxiety → anxiety.html |
     Online therapy for teens → teen.html | All conditions → conditions.html

<!-- phase:execute -->

6. Update conditions.html — activate the 4 stub cards:
   The 4 stub cards currently have no href or a "#" href and may have hub-card--stub class.
   Update each:
   - Men's Mental Health: href="mens-mental-health.html", remove stub class, add SVG icon:
     <svg viewBox="0 0 32 32" fill="none" stroke="var(--accent-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="16" cy="10" r="5"/><path d="M8 28 Q8 20 16 20 Q24 20 24 28"/><path d="M20 8 L24 4 M22 12 L27 11"/></svg>
   - Women's Mental Health: href="womens-mental-health.html", remove stub class, add SVG icon:
     <svg viewBox="0 0 32 32" fill="none" stroke="var(--accent-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="16" cy="12" r="7"/><path d="M16 19 L16 28"/><path d="M12 24 L20 24"/></svg>
   - Life Transitions: href="life-transitions.html", remove stub class, add SVG icon:
     <svg viewBox="0 0 32 32" fill="none" stroke="var(--accent-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 24 Q10 8 16 16 Q22 24 28 8"/><path d="M24 8 L28 8 L28 12"/></svg>
   - Autism & Neurodivergence: href="autism.html", remove stub class, add SVG icon:
     <svg viewBox="0 0 32 32" fill="none" stroke="var(--accent-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="16" cy="16" r="4"/><circle cx="16" cy="16" r="9"/><path d="M16 7 L16 4"/><path d="M16 28 L16 25"/><path d="M7 16 L4 16"/><path d="M28 16 L25 16"/></svg>

7. Quality gate:
   Run D:\Work\Digital-Therapy-Solutions\quality_gate.py
   All 65 pages (61 existing + 4 new) must pass — 0 failures.
   Spot-check each new page: nav links correct, breadcrumb present, hero renders,
   3 platform cards present, forks section links to correct pages, no inline <style>.
   Verify conditions.html: all 28 cards are now live-linked, none stubbed.

8. Session close:
   FRICTION PASS — collect all friction, triage FIX NOW / BACKLOG / LOG ONLY.
   Present to user before proceeding.

   MORNING_BRIEFING.md — write to D:\Work\Digital-Therapy-Solutions\MORNING_BRIEFING.md
   Schema: D:\Dev\TEMPLATES\MORNING_BRIEFING_SCHEMA.md
   Required sections: SHIPPED, QUALITY GATES, DECISIONS MADE BY AGENT,
   UNEXPECTED FINDINGS, FRICTION LOG, NEXT QUEUE

   Update STATUS.md:
   - Mark PS-CONDITIONS-02 ✅ COMPLETE with commit hash
   - Move all 4 condition pages from stub to [x] in inventory
   - Update Conditions count: 28 live / 28 total ✅ COMPLETE

   Write commit message to D:\Work\Digital-Therapy-Solutions\commit-msg.txt:
   feat(conditions): PS-CONDITIONS-02 — mens, womens, life-transitions, autism pages

   git add . && git commit -F commit-msg.txt && git push

---

CRITICAL CONSTRAINTS:
- No emoji anywhere — all icons must be inline SVG stroke-based (see icons-ban.md)
- No inline <style> blocks — all CSS already in templates/styles.css
- Asset paths: ../assets/ (output pages are one level deep)
- Stylesheet: ../templates/styles.css
- Logo img tags must include onerror fallback to initials
- Write Python scripts to file before running if needed (cmd 500 char limit)
- git commit always via commit-msg.txt + git commit -F

ACCEPTANCE CRITERIA:
- [ ] output/mens-mental-health.html exists, 3 cards, correct nav + breadcrumb
- [ ] output/womens-mental-health.html exists, 3 cards, correct nav + breadcrumb
- [ ] output/life-transitions.html exists, 3 cards, correct nav + breadcrumb
- [ ] output/autism.html exists, 3 cards, correct nav + breadcrumb
- [ ] conditions.html — all 28 cards live-linked, 0 stubs remaining
- [ ] conditions.html — 4 new SVG icons added to new cards
- [ ] quality_gate.py — 0 failures across all 65 pages
- [ ] STATUS.md updated: Conditions 28/28 ✅ COMPLETE, commit hash logged
- [ ] MORNING_BRIEFING.md written before commit
- [ ] Committed and pushed — Vercel auto-deploy triggered
