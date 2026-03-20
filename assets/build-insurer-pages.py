"""
PS-INSURANCE-01 — Build 17 stub insurer pages.
Generates well-structured, SEO-useful stub pages following aetna.html conventions exactly.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os

OUTPUT_DIR = r"D:\Work\Digital-Therapy-Solutions\output"

# Per-insurer data: (filename, display_name, logo_key, bg_color, initials, headline, coverage_status, platforms, copay_range, category_notes)
INSURERS = [
    {
        "file": "humana.html",
        "name": "Humana",
        "logo": "insurer-humana",
        "bg": "#00BCD4",
        "initials": "Hu",
        "title": "Does Humana Cover Online Therapy? Here's What We Know.",
        "meta": "Yes, Humana covers online therapy for most plans. See which platforms are in-network, what copays to expect, and how to verify your coverage.",
        "h1": "Does Humana Cover Online Therapy? Here's What We Know.",
        "subhead": "Most Humana commercial and Medicare Advantage plans cover telehealth mental health — often with the same copay as an in-person visit.",
        "follow": "Coverage varies by your specific plan and state. Use this guide to know the right questions to ask before you book.",
        "coverage": "Yes — varies by plan",
        "platforms": "Talkspace, Headway, Grow Therapy",
        "copay": "$20–50 per session with in-network providers",
        "type": "commercial",
        "extra_content": """<p>Humana offers both commercial employer plans and Medicare Advantage plans, and both categories generally cover telehealth mental health services. The Mental Health Parity Act requires Humana to cover mental health at the same level as physical health. In practice, this means most Humana members have access to video therapy sessions through in-network platforms.</p>
                    <p><strong>Medicare Advantage through Humana</strong> often includes additional telehealth benefits beyond Original Medicare — many Humana MA plans have $0 or low-copay telehealth visits for behavioral health. If you're on a Humana Gold Plus or Humana PPO plan, check your Evidence of Coverage document for telehealth mental health specifics.</p>
                    <p><strong>Commercial Humana plans</strong> vary by employer. Your HR benefits documentation or the Humana member portal (humana.com) is the fastest way to confirm your exact telehealth mental health benefits.</p>""",
        "fork1_name": "Aetna", "fork1_href": "aetna.html",
        "fork2_name": "UnitedHealthcare", "fork2_href": "unitedhealthcare.html",
        "fork3_name": "Medicare coverage", "fork3_href": "medicare.html",
    },
    {
        "file": "kaiser.html",
        "name": "Kaiser Permanente",
        "logo": "insurer-kaiser",
        "bg": "#B71C1C",
        "initials": "KP",
        "title": "Kaiser Permanente Online Therapy — What's Covered and What Isn't.",
        "meta": "Kaiser Permanente covers online therapy through its own integrated network. See what's covered, which external platforms work with Kaiser, and how to access care.",
        "h1": "Kaiser Permanente Online Therapy — What's Covered and What Isn't.",
        "subhead": "Kaiser operates an integrated care model — most mental health coverage is through Kaiser-employed therapists, not external platforms.",
        "follow": "Understanding how Kaiser works is key to getting the most from your coverage.",
        "coverage": "Yes — within Kaiser network",
        "platforms": "Kaiser's own telehealth portal (Video Visits), Talkiatry (select regions)",
        "copay": "$0–30 per telehealth visit depending on plan tier",
        "type": "integrated",
        "extra_content": """<p>Kaiser Permanente is unique among US insurers because it operates as both the insurer and the healthcare provider. Kaiser employs its own therapists and psychiatrists, and most mental health care is delivered through Kaiser's own systems rather than third-party platforms like BetterHelp or Talkspace.</p>
                    <p><strong>What this means for you:</strong> If you're a Kaiser member, your best path to covered online therapy is through Kaiser's member portal (kp.org), where you can schedule video visits with Kaiser-employed mental health providers. These are typically covered at your standard telehealth copay — often $0–30 depending on your plan tier.</p>
                    <p><strong>Third-party platforms:</strong> Most major telehealth platforms (BetterHelp, Talkspace) are not in-network with Kaiser because of this integrated model. Some Kaiser plans in certain regions have added network access to outside providers — check your specific plan documents or call Kaiser member services.</p>
                    <p><strong>Out-of-network reimbursement:</strong> Kaiser HMO plans generally do not cover out-of-network services except in emergencies. Kaiser PPO plans (available in some markets) may offer partial out-of-network reimbursement — confirm with your plan.</p>""",
        "fork1_name": "Aetna", "fork1_href": "aetna.html",
        "fork2_name": "UnitedHealthcare", "fork2_href": "unitedhealthcare.html",
        "fork3_name": "Affordable options", "fork3_href": "affordable.html",
    },
    {
        "file": "anthem.html",
        "name": "Anthem",
        "logo": "insurer-anthem",
        "bg": "#1A237E",
        "initials": "An",
        "title": "Does Anthem Cover Online Therapy? Here's What We Know.",
        "meta": "Yes, Anthem covers online therapy. See which platforms are in-network with Anthem, what copays to expect, and how to verify your specific plan.",
        "h1": "Does Anthem Cover Online Therapy? Here's What We Know.",
        "subhead": "Anthem covers telehealth mental health on most commercial plans — often with the same copay as an in-person visit.",
        "follow": "Anthem operates under different brand names by state (including some Blue Cross Blue Shield plans). This guide applies to Anthem commercial plans.",
        "coverage": "Yes — most commercial plans",
        "platforms": "Talkspace, Headway, Grow Therapy, Amwell",
        "copay": "$15–40 per session with in-network providers",
        "type": "commercial",
        "extra_content": """<p>Anthem is one of the largest commercial insurers in the United States and covers telehealth mental health services on most of its employer-sponsored and individual plans. In many states, Anthem operates as a Blue Cross Blue Shield affiliate — so if your card says Blue Cross, you may be on an Anthem plan.</p>
                    <p><strong>Telehealth parity:</strong> Anthem generally applies mental health parity rules, meaning your telehealth therapy copay should match your in-person therapy copay. On many Anthem plans, that's in the $15–40 range per session once you've met your deductible.</p>
                    <p><strong>Platform coverage:</strong> Amwell (now part of Anthem's telehealth infrastructure) is deeply integrated with Anthem plans. Talkspace, Headway, and Grow Therapy also accept Anthem in most states. When you create an account on any of these platforms, you can enter your Anthem member ID to verify coverage before your first session.</p>
                    <p><strong>Anthem Sydney app:</strong> Anthem members can also use the Sydney Health app to find in-network mental health providers and check telehealth benefits directly from their phone.</p>""",
        "fork1_name": "Blue Cross Blue Shield", "fork1_href": "bcbs.html",
        "fork2_name": "Cigna", "fork2_href": "cigna.html",
        "fork3_name": "UnitedHealthcare", "fork3_href": "unitedhealthcare.html",
    },
    {
        "file": "molina.html",
        "name": "Molina Healthcare",
        "logo": "insurer-molina",
        "bg": "#4527A0",
        "initials": "Mo",
        "title": "Molina Healthcare Mental Health Coverage — Online Therapy Options Explained.",
        "meta": "Molina Healthcare covers online therapy on most Medicaid and Marketplace plans. See which platforms work, what copays to expect, and how to access care.",
        "h1": "Molina Healthcare Mental Health Coverage — Online Therapy Options Explained.",
        "subhead": "Molina covers telehealth mental health on Medicaid and Marketplace plans in most states where it operates.",
        "follow": "Molina is Medicaid-focused — if you're on a Molina plan, this guide covers how to access online therapy through your coverage.",
        "coverage": "Yes — Medicaid and Marketplace plans",
        "platforms": "Talkspace, Grow Therapy, MDLive",
        "copay": "$0–10 per session for Medicaid; $20–40 for Marketplace plans",
        "type": "managed_behavioral",
        "extra_content": """<p>Molina Healthcare operates Medicaid managed care plans in over a dozen states, plus Marketplace plans through the ACA exchanges. Both plan types cover telehealth mental health services — Medicaid plans often at $0 copay, and Marketplace plans at a low copay after deductible.</p>
                    <p><strong>Medicaid members:</strong> If you have Molina Medicaid, mental health and substance use services are covered with little to no cost-sharing in most states. Telehealth delivery is treated the same as in-person under federal Medicaid telehealth parity rules. Check your state's Molina page for the specific platforms in-network in your state.</p>
                    <p><strong>Marketplace members:</strong> Molina Marketplace plans include mental health coverage as an Essential Health Benefit. Once you meet your deductible, telehealth therapy sessions typically cost $20–40 depending on your plan tier.</p>
                    <p><strong>Finding a provider:</strong> Log into your Molina member account at molinahealthcare.com, navigate to "Find a Provider," and filter for behavioral health and telehealth. Molina's network varies significantly by state.</p>""",
        "fork1_name": "Medicaid", "fork1_href": "medicaid.html",
        "fork2_name": "Centene", "fork2_href": "centene.html",
        "fork3_name": "Affordable options", "fork3_href": "affordable.html",
    },
]

INSURERS += [
    {
        "file": "oscar.html",
        "name": "Oscar Health",
        "logo": "insurer-oscar",
        "bg": "#F06292",
        "initials": "Os",
        "title": "Does Oscar Health Cover Online Therapy? Here's What We Know.",
        "meta": "Yes, Oscar Health covers online therapy on most plans. See which platforms are in-network, what copays to expect, and how to use Oscar's concierge team.",
        "h1": "Does Oscar Health Cover Online Therapy? Here's What We Know.",
        "subhead": "Oscar Health covers telehealth mental health on all ACA-compliant plans — and their Care Team can help you find in-network providers.",
        "follow": "Oscar is a tech-forward insurer with strong telehealth infrastructure. Here's how to make the most of your coverage.",
        "coverage": "Yes — all ACA plans",
        "platforms": "Talkspace, Headway, Grow Therapy",
        "copay": "$0–30 per session depending on plan tier",
        "type": "commercial",
        "extra_content": """<p>Oscar Health was built with telehealth at its core and covers mental health services on all its ACA-compliant Marketplace plans. Mental health is an Essential Health Benefit under the ACA, and Oscar applies parity rules — your therapy copay mirrors your primary care copay in most cases.</p>
                    <p><strong>Oscar's Care Team:</strong> One of Oscar's differentiators is their concierge Care Team, reachable through the Oscar app. If you're unsure which mental health providers are in-network, the Care Team can help navigate your options and even book appointments for you.</p>
                    <p><strong>+Oscar for employers:</strong> Oscar also offers employer-sponsored plans in some markets. If your employer uses Oscar, your mental health telehealth benefits may differ — check your Summary of Benefits.</p>
                    <p><strong>Deductible note:</strong> Some Oscar plans have $0 copay for primary care but apply a deductible to specialist visits, which may include therapy. Check your plan's Summary of Benefits and Coverage for the mental health cost-sharing row.</p>""",
        "fork1_name": "Aetna", "fork1_href": "aetna.html",
        "fork2_name": "Ambetter", "fork2_href": "ambetter.html",
        "fork3_name": "Affordable options", "fork3_href": "affordable.html",
    },
    {
        "file": "ambetter.html",
        "name": "Ambetter",
        "logo": "insurer-ambetter",
        "bg": "#388E3C",
        "initials": "Am",
        "title": "Does Ambetter Cover Online Therapy? Here's What We Know.",
        "meta": "Yes, Ambetter covers online therapy on most Marketplace plans. See which platforms are in-network, what to expect for copays, and how to verify your coverage.",
        "h1": "Does Ambetter Cover Online Therapy? Here's What We Know.",
        "subhead": "Ambetter Marketplace plans cover telehealth mental health — but coverage varies significantly by state since Ambetter is a Centene brand.",
        "follow": "Your Ambetter plan is specific to your state. Confirm telehealth mental health coverage through your state's Ambetter member portal.",
        "coverage": "Yes — varies by state",
        "platforms": "MDLive, Talkspace, Grow Therapy",
        "copay": "$5–40 per session depending on plan tier and state",
        "type": "commercial",
        "extra_content": """<p>Ambetter is the Marketplace health insurance brand of Centene Corporation, one of the largest Medicaid managed care companies in the US. Ambetter plans are sold through the ACA exchanges and are available in most states, though the exact plan features vary by state.</p>
                    <p><strong>Mental health coverage:</strong> All Ambetter plans include mental health and substance use services as an Essential Health Benefit. Telehealth mental health sessions are covered on most Ambetter plans — typically at the same copay as in-person visits once you've met your deductible.</p>
                    <p><strong>MDLive partnership:</strong> Ambetter has a preferred relationship with MDLive in many states, which means you can access virtual therapy through MDLive at your plan's telehealth copay. Log into your state's Ambetter member portal to confirm this benefit.</p>
                    <p><strong>State variation warning:</strong> Because Ambetter is run by Centene subsidiaries in each state, benefits can differ meaningfully. What's covered in Georgia may differ from Texas or Florida. Always verify through your specific state's member portal.</p>""",
        "fork1_name": "Centene", "fork1_href": "centene.html",
        "fork2_name": "Molina Healthcare", "fork2_href": "molina.html",
        "fork3_name": "Oscar Health", "fork3_href": "oscar.html",
    },
    {
        "file": "wellcare.html",
        "name": "WellCare",
        "logo": "insurer-wellcare",
        "bg": "#0277BD",
        "initials": "Wc",
        "title": "WellCare Mental Health Coverage — Online Therapy Options Explained.",
        "meta": "WellCare covers online therapy on Medicaid and Medicare Advantage plans. See what's covered, which platforms work, and how to access care.",
        "h1": "WellCare Mental Health Coverage — Online Therapy Options Explained.",
        "subhead": "WellCare's Medicaid and Medicare Advantage plans include telehealth mental health coverage — often with $0 copay for Medicaid members.",
        "follow": "WellCare is now part of Centene. If you're on a WellCare plan, your benefits are managed through Centene's network.",
        "coverage": "Yes — Medicaid and Medicare Advantage",
        "platforms": "Talkspace, MDLive, Grow Therapy",
        "copay": "$0 for Medicaid; $0–25 for Medicare Advantage",
        "type": "managed_behavioral",
        "extra_content": """<p>WellCare is a managed care organization that primarily serves Medicaid and Medicare Advantage members. WellCare was acquired by Centene Corporation in 2020 and now operates as part of Centene's broader managed care network.</p>
                    <p><strong>Medicaid members:</strong> WellCare Medicaid plans in most states cover telehealth mental health services at $0 copay. Mental health parity rules apply, and telehealth is treated equivalently to in-person care. Find WellCare-contracted behavioral health providers through your state's WellCare member portal.</p>
                    <p><strong>Medicare Advantage members:</strong> WellCare Medicare Advantage plans frequently include expanded telehealth benefits beyond Original Medicare. Many WellCare MA plans offer $0 or low-copay telehealth therapy visits. Check your plan's Annual Notice of Change for telehealth mental health details.</p>
                    <p><strong>Finding in-network providers:</strong> Use the WellCare provider finder at wellcare.com to search for behavioral health and telehealth providers in your area. Filter by "Behavioral Health" and "Telehealth" to find platforms and individual providers covered by your plan.</p>""",
        "fork1_name": "Centene", "fork1_href": "centene.html",
        "fork2_name": "Molina Healthcare", "fork2_href": "molina.html",
        "fork3_name": "Medicare", "fork3_href": "medicare.html",
    },
    {
        "file": "tricare.html",
        "name": "Tricare",
        "logo": "insurer-tricare",
        "bg": "#283593",
        "initials": "Tr",
        "title": "Does Tricare Cover Online Therapy? Coverage Guide 2026.",
        "meta": "Yes, Tricare covers online therapy for active duty, veterans, and military families. See which platforms are covered, what copays to expect, and how to access care.",
        "h1": "Does Tricare Cover Online Therapy? Coverage Guide 2026.",
        "subhead": "Tricare covers telehealth mental health for active duty service members, veterans, and military families — often at no cost.",
        "follow": "Your specific Tricare plan (Prime, Select, For Life, etc.) determines your telehealth mental health benefits. This guide covers what most plans include.",
        "coverage": "Yes — all plan types",
        "platforms": "Talkspace (military partnership), Real, Headway",
        "copay": "$0 for active duty; $0–30 for Tricare Select/Prime",
        "type": "government",
        "extra_content": """<p>Tricare is the health insurance program for US military members, retirees, and their families. All Tricare plans — Prime, Select, For Life, Young Adult, and Reserve Select — cover mental health and substance use services, including telehealth delivery.</p>
                    <p><strong>Active duty members:</strong> Active duty service members typically have $0 cost-sharing for mental health services, including telehealth therapy. Services must be from a Tricare-authorized provider.</p>
                    <p><strong>Tricare Prime and Select:</strong> Prime members pay no copay for in-network mental health services. Select members pay a cost-share (typically $25–46 per visit for mental health specialists) unless the provider is also a military treatment facility provider.</p>
                    <p><strong>Talkspace for Military:</strong> Talkspace has a dedicated military program and is a Tricare-authorized provider, making it one of the most accessible telehealth therapy options for Tricare members. You can start with your Tricare insurance information to verify coverage.</p>
                    <p><strong>Veterans:</strong> If you're a veteran using VA healthcare rather than Tricare, mental health services including telehealth are available through the VA's own network. Tricare For Life (the Medicare supplement for military retirees) also covers telehealth mental health.</p>""",
        "fork1_name": "Medicare", "fork1_href": "medicare.html",
        "fork2_name": "Medicaid", "fork2_href": "medicaid.html",
        "fork3_name": "Affordable options", "fork3_href": "affordable.html",
    },
]

INSURERS += [
    {
        "file": "chip.html",
        "name": "CHIP",
        "logo": "insurer-chip",
        "bg": "#558B2F",
        "initials": "CH",
        "title": "Does CHIP Cover Online Therapy? Coverage Guide 2026.",
        "meta": "Yes, CHIP covers online therapy for children and teens in most states. See what mental health services are covered, how telehealth works, and how to access care.",
        "h1": "Does CHIP Cover Online Therapy? Coverage Guide 2026.",
        "subhead": "The Children's Health Insurance Program covers mental health services for children and teens — including telehealth delivery in most states.",
        "follow": "CHIP is administered by each state, so benefits vary. This guide covers what most CHIP programs include for telehealth mental health.",
        "coverage": "Yes — mental health parity required",
        "platforms": "Brightline, Teen Counseling, Grow Therapy",
        "copay": "$0–5 per visit (CHIP has minimal cost-sharing by design)",
        "type": "government",
        "extra_content": """<p>CHIP — the Children's Health Insurance Program — provides low-cost health coverage to children in families that earn too much to qualify for Medicaid but can't afford private insurance. CHIP is federally funded and administered by each state, which means benefits vary somewhat by state.</p>
                    <p><strong>Mental health coverage:</strong> Federal law requires CHIP plans to cover mental health and substance use services, and the Mental Health Parity and Addiction Equity Act applies to CHIP. Most state CHIP programs cover telehealth mental health services for children and teens at little to no cost-sharing.</p>
                    <p><strong>Platforms for kids and teens:</strong> Brightline specializes in behavioral health for children and teens and accepts CHIP in several states. Teen Counseling (a BetterHelp subsidiary) focuses on teenagers but doesn't accept insurance. Grow Therapy accepts CHIP in some states and has therapists who specialize in pediatric mental health.</p>
                    <p><strong>Finding CHIP providers:</strong> Contact your state's CHIP program to get a list of in-network telehealth behavioral health providers for your child. Each state's CHIP portal has a provider directory — search for "behavioral health" and "telehealth."</p>""",
        "fork1_name": "Medicaid", "fork1_href": "medicaid.html",
        "fork2_name": "Molina Healthcare", "fork2_href": "molina.html",
        "fork3_name": "Affordable options", "fork3_href": "affordable.html",
    },
    {
        "file": "medicare.html",
        "name": "Medicare",
        "logo": "insurer-medicare",
        "bg": "#00838F",
        "initials": "Me",
        "title": "Does Medicare Cover Online Therapy? Coverage Guide 2026.",
        "meta": "Yes, Medicare covers online therapy. Original Medicare Part B covers telehealth mental health. See which platforms are covered, what copays to expect, and how to access care.",
        "h1": "Does Medicare Cover Online Therapy? Coverage Guide 2026.",
        "subhead": "Medicare Part B covers telehealth mental health services — and pandemic-era expansions made it easier to access online therapy from home.",
        "follow": "Your Medicare type (Original Medicare vs. Medicare Advantage) determines your exact telehealth options. Both cover online therapy.",
        "coverage": "Yes — Part B and most Medicare Advantage plans",
        "platforms": "Talkspace, Headway, Grow Therapy, Amwell",
        "copay": "20% of Medicare-approved amount after deductible (Original Medicare); $0–30 for most Medicare Advantage plans",
        "type": "government",
        "extra_content": """<p>Medicare covers telehealth mental health services under Part B. After the COVID-19 public health emergency expanded telehealth access, Medicare permanently extended many telehealth flexibilities — including the ability to receive mental health services via video from your home rather than requiring a healthcare facility.</p>
                    <p><strong>Original Medicare (Part B):</strong> Medicare Part B covers outpatient mental health services at 80% after you meet your Part B deductible ($240 in 2024). You pay the remaining 20% coinsurance. Telehealth mental health sessions with a Medicare-enrolled provider are covered the same as in-person visits.</p>
                    <p><strong>Medicare Advantage (Part C):</strong> Medicare Advantage plans from private insurers must cover everything Original Medicare covers — and many offer enhanced mental health telehealth benefits at lower copays. Humana, UnitedHealthcare, and Aetna's Medicare Advantage plans often have $0 telehealth copays for mental health.</p>
                    <p><strong>Eligible providers:</strong> The Medicare provider must be enrolled in Medicare and licensed to provide mental health services. Platforms like Talkspace and Headway have Medicare-enrolled providers in their networks. Always verify Medicare participation before booking.</p>""",
        "fork1_name": "Humana Medicare Advantage", "fork1_href": "humana.html",
        "fork2_name": "Tricare For Life", "fork2_href": "tricare.html",
        "fork3_name": "Affordable options", "fork3_href": "affordable.html",
    },
    {
        "file": "beacon.html",
        "name": "Beacon Health Options",
        "logo": "insurer-beacon",
        "bg": "#4E342E",
        "initials": "BH",
        "title": "Beacon Health Options Mental Health Coverage — Online Therapy Options Explained.",
        "meta": "Beacon Health Options manages behavioral health benefits for many employer plans. See how Beacon coverage works for online therapy and which platforms are in-network.",
        "h1": "Beacon Health Options Mental Health Coverage — Online Therapy Options Explained.",
        "subhead": "Beacon Health Options is a behavioral health managed care company — they manage the mental health benefits for many large employer and government plans.",
        "follow": "If your insurance card references Beacon or you get a separate behavioral health card, this guide explains how your mental health coverage works.",
        "coverage": "Yes — through contracted employer plans",
        "platforms": "Talkspace, Headway, Grow Therapy (network varies by employer contract)",
        "copay": "Depends on your primary insurance plan — typically $20–50 per session",
        "type": "managed_behavioral",
        "extra_content": """<p>Beacon Health Options (now part of Carelon Behavioral Health, owned by Elevance Health/Anthem) is a behavioral health managed care organization. Rather than being a primary insurer, Beacon manages the mental health and substance use benefits on behalf of other insurers and large employers.</p>
                    <p><strong>How Beacon works:</strong> Your primary insurance (like a Blue Cross Blue Shield or Cigna plan) may carve out mental health benefits to Beacon. This means when you need therapy, you call Beacon's member services number (found on your insurance card) rather than your primary insurer. Beacon has its own network of behavioral health providers.</p>
                    <p><strong>Telehealth coverage:</strong> Beacon-managed plans generally cover telehealth mental health services. Coverage depends on your primary employer plan, but most Beacon-contracted plans apply the same cost-sharing to telehealth as in-person visits.</p>
                    <p><strong>Finding providers:</strong> Use Beacon's provider directory at beaconhealthoptions.com (or carelon.com if your plan has transitioned to the Carelon brand) to find in-network telehealth behavioral health providers. You'll need your member ID from the Beacon/behavioral health card that came with your insurance.</p>""",
        "fork1_name": "Magellan Health", "fork1_href": "magellan.html",
        "fork2_name": "Aetna", "fork2_href": "aetna.html",
        "fork3_name": "UnitedHealthcare", "fork3_href": "unitedhealthcare.html",
    },
    {
        "file": "magellan.html",
        "name": "Magellan Health",
        "logo": "insurer-magellan",
        "bg": "#6A1B9A",
        "initials": "MG",
        "title": "Magellan Health Mental Health Coverage — Online Therapy Options Explained.",
        "meta": "Magellan Health manages behavioral health benefits for employer and government plans. See how Magellan coverage works for online therapy and which platforms are in-network.",
        "h1": "Magellan Health Mental Health Coverage — Online Therapy Options Explained.",
        "subhead": "Magellan Health is a specialty managed behavioral health organization — they handle the mental health benefits for many employer and government insurance plans.",
        "follow": "If your plan uses Magellan for behavioral health, you'll navigate mental health benefits through Magellan's network, not your primary insurer.",
        "coverage": "Yes — through contracted employer and government plans",
        "platforms": "Talkspace, Headway, MDLive (network varies by contract)",
        "copay": "Depends on primary plan — typically $20–50 per session",
        "type": "managed_behavioral",
        "extra_content": """<p>Magellan Health is a managed behavioral health organization (MBHO) that administers mental health and substance use benefits for large employers, health plans, and government programs. Like Beacon, Magellan doesn't insure you directly — they manage the behavioral health component of your existing insurance.</p>
                    <p><strong>Who uses Magellan:</strong> Magellan manages behavioral health benefits for some federal employee plans, state Medicaid programs, and large commercial employer plans. If you work for a large employer and get a separate card for "Behavioral Health" that references Magellan, your mental health benefits flow through Magellan's network.</p>
                    <p><strong>Telehealth coverage:</strong> Magellan-managed plans cover telehealth mental health services, including video therapy through Magellan's contracted providers. Coverage specifics (copay, deductible, session limits) depend on your employer's contract with Magellan.</p>
                    <p><strong>Member access:</strong> Log into the Magellan member portal at magellanhealth.com with your member ID to find in-network telehealth providers, check your benefits, and verify coverage. You can also call the Magellan member services number on your card.</p>""",
        "fork1_name": "Beacon Health Options", "fork1_href": "beacon.html",
        "fork2_name": "Cigna", "fork2_href": "cigna.html",
        "fork3_name": "Aetna", "fork3_href": "aetna.html",
    },
]

INSURERS += [
    {
        "file": "centene.html",
        "name": "Centene",
        "logo": "insurer-centene",
        "bg": "#AD1457",
        "initials": "Ce",
        "title": "Centene Mental Health Coverage — Online Therapy Options Explained.",
        "meta": "Centene covers online therapy through its Medicaid and Marketplace subsidiaries. See what's covered, which platforms work, and how to navigate Centene's state-based plans.",
        "h1": "Centene Mental Health Coverage — Online Therapy Options Explained.",
        "subhead": "Centene is the largest Medicaid managed care company in the US — its plans include Ambetter, WellCare, and state-specific Medicaid plans.",
        "follow": "You may be on a Centene plan without knowing it — if you have Ambetter, WellCare, or a state Medicaid managed care plan, Centene likely manages your benefits.",
        "coverage": "Yes — Medicaid and Marketplace plans",
        "platforms": "MDLive, Talkspace, Grow Therapy (varies by subsidiary and state)",
        "copay": "$0 for Medicaid; $5–40 for Marketplace plans",
        "type": "managed_behavioral",
        "extra_content": """<p>Centene Corporation is the largest Medicaid managed care organization in the United States and one of the largest health insurance companies overall. Centene operates through a network of subsidiaries that vary by state — including Ambetter (Marketplace), WellCare (Medicare and Medicaid), and state-specific Medicaid health plans.</p>
                    <p><strong>What Centene covers:</strong> All Centene plans — whether Medicaid, Medicare Advantage, or Marketplace — include mental health and substance use services. Telehealth delivery is covered under all plan types. The specific cost-sharing depends on your plan type and state.</p>
                    <p><strong>Medicaid plans:</strong> Centene manages Medicaid in many states under names like Peach State Health Management (Georgia), Sunshine Health (Florida), or Health Net (California). These Medicaid plans typically cover telehealth mental health at $0 copay.</p>
                    <p><strong>Finding your plan:</strong> If you're unsure whether you're on a Centene plan, look at the plan name on your insurance card and search for it alongside "Centene." Once you identify your specific plan, log into that plan's member portal to find in-network telehealth behavioral health providers.</p>""",
        "fork1_name": "Ambetter", "fork1_href": "ambetter.html",
        "fork2_name": "WellCare", "fork2_href": "wellcare.html",
        "fork3_name": "Molina Healthcare", "fork3_href": "molina.html",
    },
    {
        "file": "highmark.html",
        "name": "Highmark",
        "logo": "insurer-highmark",
        "bg": "#0D47A1",
        "initials": "Hi",
        "title": "Does Highmark Cover Online Therapy? Here's What We Know.",
        "meta": "Yes, Highmark covers online therapy. Highmark is a Blue Cross Blue Shield affiliate in PA, WV, and DE. See which platforms are covered and what to expect for copays.",
        "h1": "Does Highmark Cover Online Therapy? Here's What We Know.",
        "subhead": "Highmark is a Blue Cross Blue Shield affiliate serving Pennsylvania, West Virginia, and Delaware — with strong telehealth mental health coverage.",
        "follow": "If your card says Highmark or Highmark Blue Cross Blue Shield, this guide covers your telehealth mental health options.",
        "coverage": "Yes — most commercial plans",
        "platforms": "Talkspace, Headway, Grow Therapy, Amwell",
        "copay": "$20–50 per session with in-network providers",
        "type": "commercial",
        "extra_content": """<p>Highmark is one of the largest Blue Cross Blue Shield affiliates in the United States, primarily serving Pennsylvania, West Virginia, and Delaware. Highmark plans — including individual, employer-sponsored, and Medicare Advantage plans — cover telehealth mental health services.</p>
                    <p><strong>Telehealth parity:</strong> Highmark applies mental health parity rules, meaning your telehealth therapy copay should be comparable to your in-person therapy copay. For most Highmark commercial plans, that's in the $20–50 range per session after deductible.</p>
                    <p><strong>Amwell partnership:</strong> Highmark has an integrated relationship with Amwell, allowing Highmark members to access telehealth mental health through the Amwell platform at their in-network rate. Log into your Highmark member account to access Amwell through the Highmark portal.</p>
                    <p><strong>Highmark MyHighmark:</strong> Use the MyHighmark member portal or the Highmark app to find in-network mental health providers, check your telehealth benefits, and verify coverage before booking. Highmark's behavioral health benefits are managed in-house (not carved out to a separate MBHO).</p>""",
        "fork1_name": "Blue Cross Blue Shield", "fork1_href": "bcbs.html",
        "fork2_name": "Anthem", "fork2_href": "anthem.html",
        "fork3_name": "Cigna", "fork3_href": "cigna.html",
    },
    {
        "file": "harvard-pilgrim.html",
        "name": "Harvard Pilgrim Health Care",
        "logo": "insurer-harvard-pilgrim",
        "bg": "#BF360C",
        "initials": "HP",
        "title": "Does Harvard Pilgrim Cover Online Therapy? Here's What We Know.",
        "meta": "Yes, Harvard Pilgrim covers online therapy. See which platforms are in-network, what copays to expect, and how to access telehealth mental health through Harvard Pilgrim.",
        "h1": "Does Harvard Pilgrim Cover Online Therapy? Here's What We Know.",
        "subhead": "Harvard Pilgrim Health Care covers telehealth mental health for members in New England — with strong platform access and mental health parity.",
        "follow": "Harvard Pilgrim is now part of Point32Health alongside Tufts Health Plan. This guide covers Harvard Pilgrim plan benefits.",
        "coverage": "Yes — most commercial plans",
        "platforms": "Talkspace, Headway, Grow Therapy",
        "copay": "$20–50 per session with in-network providers",
        "type": "commercial",
        "extra_content": """<p>Harvard Pilgrim Health Care is a New England-based health insurer serving Massachusetts, New Hampshire, Maine, and Connecticut. Harvard Pilgrim merged with Tufts Health Plan in 2021 to form Point32Health, though both brands continue to operate separately.</p>
                    <p><strong>Mental health coverage:</strong> Harvard Pilgrim plans cover mental health and substance use services as required under mental health parity law. Telehealth mental health sessions are covered at your in-network copay — typically comparable to an in-person therapy visit.</p>
                    <p><strong>Finding providers:</strong> Use Harvard Pilgrim's Find a Provider tool at harvardpilgrim.org to search for in-network behavioral health providers who offer telehealth. Filter for "Behavioral Health" and "Telehealth Visits" to see which therapists and platforms are available in your area.</p>
                    <p><strong>Harvard Pilgrim + Point32Health:</strong> Since the merger with Tufts Health Plan, some Harvard Pilgrim members may have access to expanded provider networks. If you're unsure whether a platform is covered, call member services at the number on your card — they can confirm telehealth mental health benefits for your specific plan.</p>""",
        "fork1_name": "Tufts Health Plan", "fork1_href": "tufts.html",
        "fork2_name": "Blue Cross Blue Shield", "fork2_href": "bcbs.html",
        "fork3_name": "Cigna", "fork3_href": "cigna.html",
    },
    {
        "file": "tufts.html",
        "name": "Tufts Health Plan",
        "logo": "insurer-tufts",
        "bg": "#37474F",
        "initials": "Tu",
        "title": "Does Tufts Health Plan Cover Online Therapy? Here's What We Know.",
        "meta": "Yes, Tufts Health Plan covers online therapy. See which platforms are in-network, what copays to expect, and how to access telehealth mental health through Tufts.",
        "h1": "Does Tufts Health Plan Cover Online Therapy? Here's What We Know.",
        "subhead": "Tufts Health Plan covers telehealth mental health for members in Massachusetts and New England — with parity rules requiring coverage at the same level as physical health.",
        "follow": "Tufts Health Plan is now part of Point32Health alongside Harvard Pilgrim. This guide covers Tufts plan benefits.",
        "coverage": "Yes — most commercial and Medicaid plans",
        "platforms": "Talkspace, Headway, Grow Therapy",
        "copay": "$20–50 per session (commercial); $0–10 (Tufts Medicaid)",
        "type": "commercial",
        "extra_content": """<p>Tufts Health Plan is a Massachusetts-based nonprofit health insurer offering commercial, Medicare Advantage, and Medicaid plans. Tufts merged with Harvard Pilgrim Health Care in 2021 to form Point32Health, giving Tufts members access to a broader combined provider network.</p>
                    <p><strong>Telehealth mental health:</strong> All Tufts commercial plans cover telehealth mental health services under mental health parity law. Your telehealth therapy copay will typically match your in-person mental health copay — for most Tufts PPO plans, that's $20–50 per session after deductible.</p>
                    <p><strong>Tufts Medicaid (NaviCare / Tufts Health Together):</strong> Tufts manages Medicaid plans in Massachusetts. These plans cover telehealth behavioral health services at $0–10 cost-sharing. Members can access covered providers through the Tufts Health Together member portal.</p>
                    <p><strong>Medicare Advantage (Tufts Health Plan Senior Care Options):</strong> Tufts Medicare plans include telehealth mental health benefits. Coverage varies by plan — check your Evidence of Coverage for telehealth mental health cost-sharing details.</p>""",
        "fork1_name": "Harvard Pilgrim", "fork1_href": "harvard-pilgrim.html",
        "fork2_name": "Blue Cross Blue Shield", "fork2_href": "bcbs.html",
        "fork3_name": "Medicaid", "fork3_href": "medicaid.html",
    },
    {
        "file": "community-health.html",
        "name": "Community Health Plan",
        "logo": "insurer-community-health",
        "bg": "#1B5E20",
        "initials": "CP",
        "title": "Does Community Health Plan Cover Online Therapy? Here's What We Know.",
        "meta": "Community Health Plan covers online therapy for Medicaid and low-income members. See what mental health services are covered and how to access telehealth care.",
        "h1": "Does Community Health Plan Cover Online Therapy? Here's What We Know.",
        "subhead": "Community Health Plan of Washington and similar regional plans cover telehealth mental health services for Medicaid and Apple Health members.",
        "follow": "Community Health Plans vary by region. This guide focuses on Community Health Plan of Washington (CHPW) and similar regional Medicaid plans.",
        "coverage": "Yes — Medicaid and Apple Health plans",
        "platforms": "Grow Therapy, MDLive, Talkspace (varies by state)",
        "copay": "$0–5 for Medicaid members",
        "type": "commercial",
        "extra_content": """<p>Community Health Plan of Washington (CHPW) is a Medicaid managed care plan serving Apple Health (Washington State Medicaid) members. There are also community health plans in other states — this guide focuses primarily on CHPW, but the coverage principles apply broadly to similar regional plans.</p>
                    <p><strong>Mental health coverage:</strong> CHPW covers mental health and substance use services for all Apple Health members. Telehealth behavioral health sessions are covered at $0 cost-sharing for most Medicaid members. CHPW emphasizes integrated care, meaning your primary care and mental health care are coordinated.</p>
                    <p><strong>Finding telehealth providers:</strong> CHPW members can find in-network telehealth behavioral health providers through the CHPW provider directory at chpw.org. Filter for "Behavioral Health" to see therapists and counselors who offer video sessions.</p>
                    <p><strong>Not in Washington State?</strong> If you're looking for a community health plan in another state, search for your state's Medicaid program — most states have community health plan options for Medicaid-enrolled members. Coverage for telehealth mental health is generally available in all state Medicaid programs under federal parity requirements.</p>""",
        "fork1_name": "Medicaid", "fork1_href": "medicaid.html",
        "fork2_name": "Molina Healthcare", "fork2_href": "molina.html",
        "fork3_name": "Affordable options", "fork3_href": "affordable.html",
    },
]


def build_page(ins):
    name = ins["name"]
    logo = ins["logo"]
    bg = ins["bg"]
    initials = ins["initials"]
    platforms = ins["platforms"]
    copay = ins["copay"]
    coverage = ins["coverage"]
    extra = ins["extra_content"]
    f1n = ins["fork1_name"]; f1h = ins["fork1_href"]
    f2n = ins["fork2_name"]; f2h = ins["fork2_href"]
    f3n = ins["fork3_name"]; f3h = ins["fork3_href"]
    slug = ins["file"].replace(".html","")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ins["title"]} | Digital Therapy Solutions</title>
    <meta name="description" content="{ins["meta"]}">
    <link rel="icon" href="../assets/branding/favicon.png" type="image/png">
    <link rel="apple-touch-icon" href="../assets/branding/apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600&family=Instrument+Serif:ital@0;1&family=DM+Sans:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../templates/styles.css">
</head>
<body>
    <a href="#main-content" class="skip-link">Skip to main content</a>

    <nav class="site-nav">
        <div class="site-nav__inner">
            <a href="index.html" class="site-nav__brand">
                <img src="../assets/branding/logo-icon.webp" alt="" class="site-nav__brand-icon">
                Digital Therapy Solutions
            </a>
            <button class="site-nav__hamburger" aria-label="Toggle navigation">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
            </button>
            <ul class="site-nav__links">
                <li><a href="index.html">Home</a></li>
                <li><a href="conditions.html">Conditions</a></li>
                <li><a href="reviews.html">Reviews</a></li>
                <li><a href="insurance.html">Insurance</a></li>
                <li><a href="about.html">About</a></li>
            </ul>
        </div>
    </nav>

    <main id="main-content">
    <nav aria-label="Breadcrumb" class="breadcrumb" style="max-width:var(--table-width);margin:0 auto;padding:var(--space-xs) var(--space-md);">
        <a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="insurance.html">Insurance</a><span class="breadcrumb__sep">/</span>{name}
    </nav>

        <div class="section-wrapper section-wrapper--hero">
            <div class="hero-visual">
                <img src="../assets/hero.webp" alt="Person reviewing insurance coverage for online therapy" class="hero-image">
            </div>
            <div class="hero-text">
                <div style="width:64px;height:64px;border-radius:12px;background:{bg};color:#fff;font-weight:700;font-size:1.2rem;display:flex;align-items:center;justify-content:center;margin-bottom:var(--space-sm);">
                    <img src="../assets/logos/{logo}.webp" alt="{name} logo" style="width:100%;height:100%;object-fit:contain;border-radius:12px;" onerror="this.style.display='none';this.parentElement.textContent='{initials}';">
                </div>
                <h1>{ins["h1"]}</h1>
                <p class="hero-subhead"><em>{ins["subhead"]}</em></p>
                <p class="hero-subhead hero-subhead--follow">{ins["follow"]}</p>
                <div class="trust-row">
                    <span>34+ Platforms Reviewed</span>
                    <span>Expert-Written</span>
                    <span>Updated 2026</span>
                    <span>No Sponsored Rankings</span>
                </div>
            </div>
        </div>

        <svg class="section-divider" viewBox="0 0 1440 48" preserveAspectRatio="none" aria-hidden="true"><path d="M0 48h1440V24C1200 42 960 8 720 24S240 42 0 24v24z" fill="#F5F0E8"/></svg>

        <div class="section-wrapper section-wrapper--alt" id="coverage">
            <div class="content-container">
                <h2 class="section-heading">{name} and Online Therapy — What We Know</h2>
                <div class="reveal">
                    <p><strong>Coverage status:</strong> {coverage}</p>
                    <p><strong>Platforms commonly in-network:</strong> {platforms}</p>
                    <p><strong>Typical cost with insurance:</strong> {copay}</p>
                    {extra}
                </div>
            </div>
        </div>

        <svg class="section-divider section-divider--flip" viewBox="0 0 1440 48" preserveAspectRatio="none" aria-hidden="true"><path d="M0 0h1440v24C1200 6 960 40 720 24S240 6 0 24V0z" fill="#F5F0E8"/></svg>

        <div class="section-wrapper">
            <div class="content-container">
                <h2 class="section-heading">What to Expect</h2>
                <div class="reveal">
                    <p>Most plans that cover online therapy work the same way as in-person coverage. Once you're matched with an in-network provider, you pay your plan's mental health copay per session. If you haven't met your deductible yet, you may pay more until you hit that threshold — then your copay rate applies for the rest of the year.</p>
                    <p><strong>Typical copay range:</strong> {copay}. Keep in mind this is an estimate — your actual cost depends on your specific plan, your deductible status, and whether the provider is in-network.</p>
                    <p>Always verify your exact coverage before your first session. Most platforms let you enter your insurance information during signup and will confirm whether you're covered before you pay anything.</p>
                </div>
            </div>
        </div>

        <div class="section-wrapper section-wrapper--alt">
            <div class="content-container">
                <h2 class="section-heading">How to Check Your {name} Coverage</h2>
                <div class="reveal">
                    <ol>
                        <li>Call the member services number on the back of your {name} card and ask: "Does my plan cover telehealth mental health services?"</li>
                        <li>Ask specifically: "Is telehealth therapy covered at the same copay as in-person therapy?"</li>
                        <li>Ask: "Which telehealth platforms are in-network for mental health? Is [platform name] covered?"</li>
                        <li>Ask: "What is my current deductible status for mental health benefits?"</li>
                    </ol>
                    <p>Alternatively, log into your {name} member portal online and navigate to "Benefits" or "Coverage Details" — look for the "Mental Health" or "Behavioral Health" section. Most member portals show your specific copay and deductible information.</p>
                </div>
            </div>
        </div>

        <div class="section-wrapper section-wrapper--accent">
            <div class="content-container forks-section">
                <div class="forks-layout reveal">
                    <div class="forks-text">
                        <h3 class="forks-heading"><em>More resources</em></h3>
                        <div class="forks-links">
                            <a href="insurance.html" class="fork-link">Compare all insurance options <span>→</span></a>
                            <a href="betterhelp-review.html" class="fork-link">BetterHelp review — platforms commonly covered <span>→</span></a>
                            <a href="talkspace-review.html" class="fork-link">Talkspace review — platforms commonly covered <span>→</span></a>
                            <a href="{f1h}" class="fork-link">{f1n} coverage guide <span>→</span></a>
                            <a href="{f2h}" class="fork-link">{f2n} coverage guide <span>→</span></a>
                            <a href="{f3h}" class="fork-link">{f3n} <span>→</span></a>
                        </div>
                    </div>
                    <div class="forks-image">
                        <img src="../assets/video-call-earbuds.webp" alt="Person on couch with earbuds during an online therapy session" class="forks-image__img">
                    </div>
                </div>
            </div>
        </div>

        <div class="section-wrapper section-wrapper--alt">
            <div class="content-container" style="text-align:center;padding:var(--space-xl) var(--space-md);">
                <h2 class="section-heading">Ready to Compare All Your Options?</h2>
                <p style="margin-bottom:var(--space-md);">See all 23 insurers and compare coverage options side by side.</p>
                <a href="insurance.html" class="cta-button">Compare All Insurance Options</a>
            </div>
        </div>

        <div class="section-wrapper section-wrapper--muted" id="disclosures">
            <div class="content-container">
                <div class="disclaimers">
                    <p>We're not therapists or insurance advisors — we're researchers who compiled publicly available information about insurance coverage for online therapy. Coverage information is general and may not reflect your specific plan. Always verify your exact benefits directly with {name} before booking a session. Some links on this page may be affiliate links.</p>
                    <p>Insurance coverage depends on your specific plan, state, and provider. Copay estimates are based on averages and may vary significantly. We update regularly, but confirm current coverage directly with your insurer.</p>
                </div>
            </div>
        </div>
    </main>

    <footer class="site-footer">
        <div class="site-footer__inner">
            <div>
                <h3>About Digital Therapy Solutions</h3>
                <p>Independent reviews of online therapy platforms. Expert-written, regularly updated, no sponsored rankings.</p>
            </div>
            <div>
                <h3>Quick Links</h3>
                <ul><li><a href="index.html">Home</a></li><li><a href="betterhelp-review.html">Platform Reviews</a></li><li><a href="insurance.html">Insurance Guide</a></li><li><a href="about.html">About Us</a></li></ul>
            </div>
            <div>
                <h3>Resources</h3>
                <ul><li><a href="editorial-policy.html">Editorial Policy</a></li><li><a href="affiliate-disclosure.html">Affiliate Disclosure</a></li><li><a href="privacy-policy.html">Privacy Policy</a></li></ul>
            </div>
        </div>
        <div class="site-footer__crisis"><span class="crisis-alert">In crisis?</span> Call or text <a href="tel:988">988</a> &middot; Text HOME to <a href="sms:741741">741741</a> &middot; Emergency: <a href="tel:911">911</a></div>
        <div class="site-footer__bottom">&copy; 2026 Digital Therapy Solutions. All rights reserved. | <a href="privacy-policy.html">Privacy</a> | <a href="affiliate-disclosure.html">Disclosures</a></div>
    </footer>

    <script>
        const hamburger = document.querySelector('.site-nav__hamburger');
        const navLinks = document.querySelector('.site-nav__links');
        if (hamburger && navLinks) {{
            hamburger.addEventListener('click', () => navLinks.classList.toggle('open'));
        }}
        const reveals = document.querySelectorAll('.reveal');
        const revealObserver = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    entry.target.classList.add('visible');
                    revealObserver.unobserve(entry.target);
                }}
            }});
        }}, {{ threshold: 0.15, rootMargin: '0px 0px -40px 0px' }});
        reveals.forEach(el => revealObserver.observe(el));
        const btt = document.createElement('button');
        btt.className = 'back-to-top';
        btt.innerHTML = '&#8593;';
        btt.setAttribute('aria-label', 'Back to top');
        document.body.appendChild(btt);
        window.addEventListener('scroll', () => {{
            btt.classList.toggle('visible', window.scrollY > 600);
        }});
        btt.addEventListener('click', () => {{
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }});
    </script>
</body>
</html>"""

# Generate all pages
print(f"Building {len(INSURERS)} insurer pages...\n")
for ins in INSURERS:
    fpath = os.path.join(OUTPUT_DIR, ins["file"])
    html = build_page(ins)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  {ins['file']}: written ({len(html)} chars)")

print(f"\nDone. {len(INSURERS)} pages written to {OUTPUT_DIR}")
