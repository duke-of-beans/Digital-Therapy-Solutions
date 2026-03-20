import os, re

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

# Fix any remaining absolute link issues in new pages
new_pages = ['about.html','affiliate-disclosure.html','crisis-resources.html',
             'do-i-need-therapy.html','editorial-policy.html','how-online-therapy-works.html',
             'privacy-policy.html']

# index.html has its own special treatment (different asset paths)
# Check it separately

fixes = {
    'href="/conditions"': 'href="anxiety.html"',
    'href="/insurance"': 'href="aetna.html"',
    'href="/reviews"': 'href="betterhelp-review.html"',
    'href="/about"': 'href="about.html"',
    'href="/privacy"': 'href="privacy-policy.html"',
    'href="/terms"': 'href="privacy-policy.html"',
    'href="/editorial-policy"': 'href="editorial-policy.html"',
    'href="/affiliate-disclosure"': 'href="affiliate-disclosure.html"',
    'href="/"': 'href="index.html"',
    'href="/do-i-need-therapy"': 'href="do-i-need-therapy.html"',
    'href="/how-online-therapy-works"': 'href="how-online-therapy-works.html"',
    'href="/crisis-resources"': 'href="crisis-resources.html"',
}

for fname in new_pages + ['index.html']:
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    for old, new in fixes.items():
        content = content.replace(old, new)
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed absolute links: {fname}')
    else:
        print(f'Clean: {fname}')

# Special check for index.html asset paths
with open(os.path.join(output_dir, 'index.html'), 'r', encoding='utf-8') as f:
    idx_content = f.read()

# index.html should use assets/branding/ NOT ../assets/branding/
# Check
if '../assets/branding/' in idx_content:
    idx_content = idx_content.replace('../assets/branding/', 'assets/branding/')
    idx_content = idx_content.replace('../assets/logos/', 'assets/logos/')
    idx_content = idx_content.replace('../assets/hero.webp', 'assets/hero.webp')
    idx_content = idx_content.replace('../templates/styles.css', '../templates/styles.css')  # keep this one
    with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(idx_content)
    print('Fixed index.html asset paths (removed ../ prefix for branding/logos)')
else:
    print('index.html asset paths OK')

print('Done.')
