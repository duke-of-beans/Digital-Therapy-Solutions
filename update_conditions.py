#!/usr/bin/env python3
"""Convert stub cards in conditions.html to live links."""
import re

PATH = r'D:\Work\Digital-Therapy-Solutions\output\conditions.html'

# Map of condition name text to slug
SLUG_MAP = {
    'OCD': 'ocd.html',
    'PTSD': 'ptsd.html',
    'Bipolar Disorder': 'bipolar.html',
    'Eating Disorders': 'eating-disorders.html',
    'Grief': 'grief.html',
    'Addiction': 'addiction.html',
    'Postpartum': 'postpartum.html',
    'Teen Mental Health': 'teen.html',
    'Anger Management': 'anger.html',
    'Loneliness': 'loneliness.html',
    'Self-Esteem': 'self-esteem.html',
    'Stress': 'stress.html',
    'LGBTQ+': 'lgbtq.html',
    "Men's Mental Health": None,   # not in this sprint - keep stub
    "Women's Mental Health": None, # not in this sprint - keep stub
    'Insomnia': 'insomnia.html',
    'Chronic Illness': 'chronic-pain.html',
    'Relationship Issues': 'relationship.html',
    'Life Transitions': None,      # not in this sprint - keep stub
    'Autism': None,                # not in this sprint - keep stub
    'Burnout': 'burnout.html',
    'Social Anxiety': 'social-anxiety.html',
    'Phobias': 'phobias.html',
    'Panic': 'panic.html',
}

# The 20 slugs we're activating
ACTIVATE = {
    'ocd.html', 'ptsd.html', 'bipolar.html', 'eating-disorders.html', 'grief.html',
    'anger.html', 'addiction.html', 'stress.html', 'relationship.html', 'lgbtq.html',
    'teen.html', 'postpartum.html', 'burnout.html', 'insomnia.html', 'chronic-pain.html',
    'social-anxiety.html', 'phobias.html', 'panic.html', 'loneliness.html', 'self-esteem.html',
}

with open(PATH, 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# Strategy: find each stub card block and convert it
# A stub card looks like:
#   <div class="hub-card hub-card--stub">
#       <div style="font-size:2rem;">EMOJI</div>
#       <div class="hub-card__name">NAME</div>
#       <div class="hub-card__desc">DESC</div>
#       <span class="hub-card__cta">Guide Coming</span>
#   </div>
#
# We need to convert to the live card pattern (matching anxiety/depression/adhd/couples):
#   <div class="hub-card">
#       <div style="font-size:2rem;">EMOJI</div>
#       <div class="hub-card__name">NAME</div>
#       <div class="hub-card__desc">DESC</div>
#       <a href="SLUG" class="hub-card__cta">Read Guide →</a>
#   </div>

# Find all stub card blocks
stub_pattern = re.compile(
    r'(<div class="hub-card hub-card--stub">.*?<div class="hub-card__name">(.*?)</div>.*?)<span class="hub-card__cta">Guide Coming</span>(\s*</div>)',
    re.DOTALL
)

conversions = 0
failed = []

def replace_stub(m):
    global conversions
    pre = m.group(1)
    name_raw = m.group(2).strip()
    closing = m.group(3)
    
    # Determine slug
    slug = None
    for key, s in SLUG_MAP.items():
        if key.lower() in name_raw.lower() or name_raw.lower() in key.lower():
            slug = s
            break
    
    if slug is None or slug not in ACTIVATE:
        # Not activating this one - leave as stub
        return m.group(0)
    
    # Convert: remove hub-card--stub class, replace span with <a>
    converted_pre = pre.replace('hub-card hub-card--stub', 'hub-card')
    result = converted_pre + f'<a href="{slug}" class="hub-card__cta">Read Guide &rarr;</a>' + closing
    conversions += 1
    print(f'  Activated: {name_raw} -> {slug}')
    return result

new_html = stub_pattern.sub(replace_stub, html)

# Also update the section-context paragraph (4 live -> 24 live)
new_html = new_html.replace(
    '4 full guides live. 20 more in progress — check back as we publish.',
    '24 full guides live &mdash; updated monthly.'
)

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f'\nconversions: {conversions}')
print(f'File updated: {PATH}')

# Verify: count remaining stubs
remaining = new_html.count('hub-card--stub')
print(f'Remaining stubs: {remaining}')

# Count live cards (hub-card without --stub)
live = len(re.findall(r'class="hub-card"', new_html))
print(f'Live cards: {live}')
