import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

OUTPUT_DIR = Path(r'D:\Work\Digital-Therapy-Solutions\output')

# Map insurer slug -> display details for the stat callout and section headings
insurers = {
    'bcbs': {
        'name': 'BCBS',
        'copay': '$15',
        'copay_label': 'avg copay with BCBS in-network',
        'coverage_heading': 'How BCBS Coverage Works for Online Therapy',
        'whatif_heading': "What If My BCBS Plan Isn't Accepted?",
        'coverage_intro': 'Most Blue Cross Blue Shield plans — PPO, HMO, and employer-sponsored — cover online therapy the same way they cover in-person sessions.',
        'copay_text': 'Most BCBS members pay $15–50 per therapy session with an in-network platform — significantly less than the $150–300 out-of-pocket rate.',
        'eap_text': 'BCBS',
        'whatif_intro': "Not every BCBS plan works with every platform. If you get a \"not covered\" result, you still have options:",
        'oon_text': 'Many BCBS PPO plans cover out-of-network mental health at 50–70% after deductible.',
        'eap_label': 'BCBS EAP',
        'eap_desc': "Even if your therapy coverage is limited, your employer's EAP through BCBS may offer free sessions — typically 3–8 — as a separate benefit.",
        'affordable_link': 'affordable.html',
    },
    'cigna': {
        'name': 'Cigna',
        'copay': '$20',
        'copay_label': 'avg copay with Cigna in-network',
        'coverage_heading': 'How Cigna Coverage Works for Online Therapy',
        'whatif_heading': "What If My Cigna Plan Isn't Accepted?",
        'coverage_intro': 'Most Cigna plans — including Open Access Plus (OAP), HMO, and employer-sponsored plans — cover online therapy the same way they cover in-person sessions.',
        'copay_text': 'Most Cigna members pay $20–50 per therapy session with an in-network platform — significantly less than the $150–300 out-of-pocket rate.',
        'eap_text': 'Cigna',
        'whatif_intro': "Not every Cigna plan works with every platform. If you get a \"not covered\" result, you still have options:",
        'oon_text': 'Many Cigna OAP plans cover out-of-network mental health at 50–70% after deductible.',
        'eap_label': 'Cigna EAP',
        'eap_desc': "Even if your therapy coverage is limited, your employer's EAP through Cigna may offer free sessions — typically 3–8 — as a separate benefit.",
        'affordable_link': 'affordable.html',
    },
}

STAT_BLOCK = '''<div class="split-section reveal">
<div class="split-section__main">
{prose}
</div>
<div class="split-section__aside">
<div class="stat-callout">
<div class="stat-callout__number">{copay}</div>
<div class="stat-callout__label">{copay_label}</div>
</div>
</div>
</div>'''

FEATURE_LIST_BLOCK = '''<div class="feature-list reveal">
<div class="feature-list__item">
<svg class="feature-list__icon feature-list__icon--positive" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>
<div class="feature-list__content">
<div class="feature-list__title">Out-of-network reimbursement</div>
<div class="feature-list__desc">{oon_text} Pay upfront, submit a claim for partial reimbursement. Call the number on the back of your card to check your out-of-network mental health benefits.</div>
</div>
</div>
<div class="feature-list__item">
<svg class="feature-list__icon feature-list__icon--positive" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>
<div class="feature-list__content">
<div class="feature-list__title">{eap_label}</div>
<div class="feature-list__desc">{eap_desc}</div>
</div>
</div>
<div class="feature-list__item">
<svg class="feature-list__icon feature-list__icon--positive" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>
<div class="feature-list__content">
<div class="feature-list__title">Financial assistance programs</div>
<div class="feature-list__desc">BetterHelp offers financial aid that can reduce costs by 10–40%. Calmerry starts at $42/week without insurance. Both are affordable alternatives when insurance doesn\'t apply.</div>
</div>
</div>
<div class="feature-list__item">
<svg class="feature-list__icon feature-list__icon--positive" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>
<div class="feature-list__content">
<div class="feature-list__title">Affordable self-pay alternatives</div>
<div class="feature-list__desc">See our <a href="{affordable_link}">guide to affordable online therapy</a> for platforms starting at $30/session with no insurance required.</div>
</div>
</div>
</div>'''

for slug, info in insurers.items():
    filepath = OUTPUT_DIR / f'{slug}.html'
    if not filepath.exists():
        print(f'SKIP (not found): {slug}.html')
        continue

    content = filepath.read_text(encoding='utf-8')
    original = content
    changed = False

    # 1. Find coverage section and wrap in split-section + stat-callout
    # Look for the section with coverage heading
    import re

    # Pattern: find the prose div inside the coverage section
    # We look for <div class="reveal"> following the coverage heading and replace with split-section
    cov_pattern = r'(<h2 class="section-heading">How ' + re.escape(info['name']) + r' Coverage Works[^<]*</h2>\s*)<div class="reveal">(.*?)</div>\s*</div>\s*</div>'
    
    def build_prose(m):
        inner = m.group(2)
        stat = STAT_BLOCK.format(
            prose=f'<div class="reveal">{inner}</div>',
            copay=info['copay'],
            copay_label=info['copay_label']
        )
        return m.group(1) + stat + '\n</div>\n</div>'
    
    new_content, n = re.subn(cov_pattern, build_prose, content, flags=re.DOTALL)
    if n:
        content = new_content
        changed = True
        print(f'  PATCHED coverage split-section: {slug}.html ({n} replacements)')
    else:
        print(f'  WARN: coverage pattern not matched in {slug}.html')

    # 2. Find "What If" section and convert prose to feature-list
    whatif_pattern = r'(<h2 class="section-heading">What If My ' + re.escape(info['name']) + r" Plan[^<]*</h2>\s*)<div class=\"reveal\">(.*?)</div>\s*</div>\s*</div>"
    
    def build_whatif(m):
        fl = FEATURE_LIST_BLOCK.format(
            oon_text=info['oon_text'],
            eap_label=info['eap_label'],
            eap_desc=info['eap_desc'],
            affordable_link=info['affordable_link']
        )
        intro_p = f'<p>{info["whatif_intro"]}</p>\n'
        return m.group(1) + intro_p + fl + '\n</div>\n</div>'
    
    new_content, n = re.subn(whatif_pattern, build_whatif, content, flags=re.DOTALL)
    if n:
        content = new_content
        changed = True
        print(f'  PATCHED whatif feature-list: {slug}.html ({n} replacements)')
    else:
        print(f'  WARN: whatif pattern not matched in {slug}.html')

    if changed:
        filepath.write_text(content, encoding='utf-8')
        print(f'  SAVED: {slug}.html')
    else:
        print(f'  NO CHANGES: {slug}.html')

print('\nDone.')
