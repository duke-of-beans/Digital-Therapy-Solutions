"""
PS-IMAGE-01 — Tier 1 Hero Differentiation Patch
Assigns the correct hero image to each page cluster.
Run from: D:\Work\Digital-Therapy-Solutions\
"""

import os
import re

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')

# Page → hero mapping
HERO_MAP = {
    'hero-home.webp': [
        'index.html',
    ],
    'hero-emotional.webp': [
        'anxiety.html', 'depression.html', 'ptsd.html', 'ocd.html',
        'grief.html', 'loneliness.html', 'self-esteem.html',
        'eating-disorders.html', 'anger.html', 'addiction.html',
        'panic.html', 'phobias.html', 'insomnia.html', 'chronic-pain.html',
        'social-anxiety.html', 'postpartum.html', 'lgbtq.html',
        'mens-mental-health.html', 'womens-mental-health.html',
        'life-transitions.html', 'autism.html', 'bipolar.html',
        'teen.html',
        'teen-counseling-review.html', 'brightline-review.html',
        'manatee-health-review.html', 'lunajoy-review.html',
    ],
    'hero-focus.webp': [
        'adhd.html', 'burnout.html', 'stress.html',
        'adhd-online-review.html', 'done-adhd-review.html',
        'circle-medical-review.html', 'klarity-review.html',
    ],
    'hero-couples.webp': [
        'couples.html', 'relationship.html',
        'our-relationship-review.html', 'our-ritual-review.html',
        'regain-review.html',
    ],
    'hero-practical.webp': [
        'aetna.html', 'bcbs.html', 'cigna.html', 'unitedhealthcare.html',
        'medicaid.html', 'affordable.html', 'humana.html', 'kaiser.html',
        'anthem.html', 'molina.html', 'oscar.html', 'ambetter.html',
        'wellcare.html', 'tricare.html', 'chip.html', 'medicare.html',
        'beacon.html', 'magellan.html', 'centene.html', 'highmark.html',
        'harvard-pilgrim.html', 'tufts.html', 'community-health.html',
    ],
}

# All remaining pages (review pages not otherwise assigned) get hero-review.webp
REVIEW_FALLBACK = 'hero-review.webp'

# Build reverse lookup
page_to_hero = {}
for hero, pages in HERO_MAP.items():
    for page in pages:
        page_to_hero[page] = hero

patched = []
skipped = []
errors = []

for filename in os.listdir(OUTPUT_DIR):
    if not filename.endswith('.html'):
        continue

    hero = page_to_hero.get(filename, REVIEW_FALLBACK)
    filepath = os.path.join(OUTPUT_DIR, filename)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Only patch if still using the old generic hero
        if 'src="../assets/hero.webp"' not in content:
            skipped.append(f'  SKIP (already patched or no hero): {filename}')
            continue

        new_content = content.replace(
            'src="../assets/hero.webp"',
            f'src="../assets/{hero}"'
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        patched.append(f'  {filename} → {hero}')

    except Exception as e:
        errors.append(f'  ERROR {filename}: {e}')

print(f'\nPS-IMAGE-01 Tier 1 Hero Patch')
print(f'{"="*50}')
print(f'Patched: {len(patched)}')
for p in sorted(patched):
    print(p)

if skipped:
    print(f'\nSkipped: {len(skipped)}')
    for s in sorted(skipped):
        print(s)

if errors:
    print(f'\nErrors: {len(errors)}')
    for e in errors:
        print(e)

print(f'\nDone.')
