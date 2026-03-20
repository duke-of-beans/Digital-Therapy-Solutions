"""
patch_hub_nav.py — PS-HUB-01
Updates nav links in all 21 output pages:
  anxiety.html      → conditions.html
  betterhelp-review.html → reviews.html
  aetna.html        → insurance.html
"""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

OLD_LINKS = [
    ('<li><a href="anxiety.html">Conditions</a></li>', '<li><a href="conditions.html">Conditions</a></li>'),
    ('<li><a href="betterhelp-review.html">Reviews</a></li>', '<li><a href="reviews.html">Reviews</a></li>'),
    ('<li><a href="aetna.html">Insurance</a></li>', '<li><a href="insurance.html">Insurance</a></li>'),
]

files = [f for f in os.listdir(output_dir) if f.endswith('.html')]
changed = []
skipped = []

for fname in sorted(files):
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    for old, new in OLD_LINKS:
        new_content = new_content.replace(old, new)

    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        changed.append(fname)
    else:
        skipped.append(fname)

print(f'Updated ({len(changed)}):')
for f in changed:
    print(f'  ✅ {f}')
print(f'\nSkipped / already correct ({len(skipped)}):')
for f in skipped:
    print(f'  — {f}')
