"""
patch_heroes.py — PS-IMAGE-01 Tier 1
Replaces hero image src + alt on every output HTML page
based on page-type cluster assignment.
"""

import os
import re

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'output')

# --- Cluster definitions ---

HERO_MAP = {
    # Homepage
    'index.html': ('hero-home.webp', 'Woman on couch with laptop — exploring online therapy options from home'),

    # Emotional cluster
    'anxiety.html':          ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for anxiety'),
    'depression.html':       ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for depression'),
    'ptsd.html':             ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for PTSD'),
    'ocd.html':              ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for OCD'),
    'grief.html':            ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for grief'),
    'loneliness.html':       ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for loneliness'),
    'self-esteem.html':      ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for self-esteem'),
    'postpartum.html':       ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for postpartum support'),
    'insomnia.html':         ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for insomnia'),
    'panic.html':            ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for panic disorder'),
    'phobias.html':          ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for phobias'),
    'social-anxiety.html':   ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for social anxiety'),
    'bipolar.html':          ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for bipolar disorder'),
    'eating-disorders.html': ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for eating disorders'),
    'addiction.html':        ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for addiction'),
    'chronic-pain.html':     ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for chronic pain'),
    'lgbtq.html':            ('hero-emotional.webp', 'Person by window in quiet reflection — affirming online therapy'),
    'mens-mental-health.html':   ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for men'),
    'womens-mental-health.html': ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for women'),
    'life-transitions.html': ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for life transitions'),
    'autism.html':           ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for autism support'),
    'teen.html':             ('hero-emotional.webp', 'Person by window in quiet reflection — online therapy for teens'),
    'how-online-therapy-works.html': ('hero-emotional.webp', 'Person by window in quiet reflection — how online therapy works'),
    'do-i-need-therapy.html':       ('hero-emotional.webp', 'Person by window in quiet reflection — do I need therapy?'),

    # Focus cluster
    'adhd.html':    ('hero-focus.webp', 'Person at desk with multiple screens — online therapy for ADHD'),
    'burnout.html': ('hero-focus.webp', 'Person at desk focused on work — online therapy for burnout'),
    'stress.html':  ('hero-focus.webp', 'Person at desk managing workload — online therapy for stress'),
    'anger.html':   ('hero-focus.webp', 'Person at desk in focused moment — online therapy for anger management'),

    # Couples cluster
    'couples.html':      ('hero-couples.webp', 'Two people in warm conversation — online couples therapy'),
    'relationship.html': ('hero-couples.webp', 'Two people connecting — online relationship therapy'),

    # Hub pages
    'reviews.html':    ('hero-review.webp',    'Person with coffee and laptop — comparing online therapy platforms'),
    'conditions.html': ('hero-emotional.webp', 'Person by window in quiet reflection — find therapy for your condition'),
    'insurance.html':  ('hero-practical.webp', 'Person on phone at home — does your insurance cover online therapy?'),
}

# All review pages → hero-review.webp
REVIEW_PAGES = [
    'betterhelp-review.html', 'talkspace-review.html', 'online-therapy-com-review.html',
    'adhd-online-review.html', 'amwell-review.html', 'bend-health-review.html',
    'brightline-review.html', 'brightside-review.html', 'calmerry-review.html',
    'cerebral-review.html', 'circle-medical-review.html', 'doctor-on-demand-review.html',
    'done-adhd-review.html', 'faithful-counseling-review.html', 'gay-therapy-center-review.html',
    'grow-therapy-review.html', 'headspace-review.html', 'headway-review.html',
    'inclusive-therapists-review.html', 'klarity-review.html', 'lunajoy-review.html',
    'manatee-health-review.html', 'mindful-care-review.html', 'nocd-review.html',
    'open-path-review.html', 'our-relationship-review.html', 'our-ritual-review.html',
    'pride-counseling-review.html', 'psychology-today-review.html', 'regain-review.html',
    'simplepractice-review.html', 'talkiatry-review.html', 'teen-counseling-review.html',
    'therapyden-review.html',
]

# All insurance pages → hero-practical.webp
INSURANCE_PAGES = [
    'aetna.html', 'bcbs.html', 'cigna.html', 'unitedhealthcare.html', 'medicaid.html',
    'affordable.html', 'humana.html', 'kaiser.html', 'anthem.html', 'molina.html',
    'oscar.html', 'ambetter.html', 'wellcare.html', 'tricare.html', 'chip.html',
    'medicare.html', 'beacon.html', 'magellan.html', 'centene.html', 'highmark.html',
    'harvard-pilgrim.html', 'tufts.html', 'community-health.html',
]

for page in REVIEW_PAGES:
    HERO_MAP[page] = ('hero-review.webp', 'Person with coffee and laptop — researching online therapy platforms')

for page in INSURANCE_PAGES:
    if page not in HERO_MAP:
        HERO_MAP[page] = ('hero-practical.webp', 'Person on phone at home — navigating insurance and therapy options')

# --- Regex pattern to match the hero-image img tag ---
# Matches: <img alt="..." class="hero-image" src="..."/>
# OR:      <img alt="..." class="hero-image" src="...">
HERO_PATTERN = re.compile(
    r'(<img\s[^>]*class="hero-image"[^>]*>)',
    re.DOTALL
)

SRC_PATTERN  = re.compile(r'src="[^"]*"')
ALT_PATTERN  = re.compile(r'alt="[^"]*"')

patched = 0
skipped = 0
not_found = 0

for filename, (hero_file, alt_text) in HERO_MAP.items():
    filepath = os.path.join(OUTPUT_DIR, filename)
    if not os.path.exists(filepath):
        print(f'  [MISSING]  {filename}')
        not_found += 1
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    match = HERO_PATTERN.search(content)
    if not match:
        print(f'  [NO HERO]  {filename}')
        skipped += 1
        continue

    original_tag = match.group(1)
    new_src = f'src="../assets/{hero_file}"'
    new_alt = f'alt="{alt_text}"'

    new_tag = SRC_PATTERN.sub(new_src, original_tag)
    new_tag = ALT_PATTERN.sub(new_alt, new_tag, count=1)  # only first alt (the hero one)

    if new_tag == original_tag:
        print(f'  [ALREADY]  {filename}')
        skipped += 1
        continue

    new_content = content.replace(original_tag, new_tag, 1)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f'  [PATCHED]  {filename} → {hero_file}')
    patched += 1

print(f'\nDone. Patched: {patched} | Skipped: {skipped} | Missing: {not_found}')
