"""Replace all Sarah Chen references with DTS Research Team editorial framing."""
import re, os, glob

BASE = r'D:\Work\Digital-Therapy-Solutions'
OUT = os.path.join(BASE, 'output')

bp = os.path.join(BASE, 'build_pages.py')
with open(bp, 'r', encoding='utf-8') as f:
    content = f.read()

bio = 'Every recommendation on this page was independently researched, cross-referenced against current clinical literature, and verified for accuracy by the DTS editorial team. Platforms are re-evaluated monthly.'

content = re.sub(
    r"'reviewer_bio':\s*['\"]Dr\. Chen is[^'\"]*['\"]",
    f"'reviewer_bio': '{bio}'",
    content
)
with open(bp, 'w', encoding='utf-8') as f:
    f.write(content)
count_bp = len(re.findall('DTS editorial team', content))
print(f'build_pages.py: {count_bp} reviewer_bio replacements')

replacements = [
    (r'personally tested and clinically reviewed by <strong>Dr\. Sarah Chen, LCSW</strong>[^<]*',
     'independently evaluated by the <strong>DTS Research Team</strong> using our 12-point clinical accuracy standard.'),
    ('Reviewed by Dr. Sarah Chen, LCSW', 'Editorially reviewed \u00b7 DTS Research Team'),
    ('About Our Reviewer', 'About Our Editorial Process'),
    (r'class="reviewer-card__avatar">SC<', 'class="reviewer-card__avatar">DTS<'),
    (r'Dr\.\s*Sarah\s*Chen\s*<span class="credential-badge">LCSW</span>',
     'DTS Research Team <span class="credential-badge">Editorial</span>'),
    (r'Dr\. Chen is a Licensed Clinical Social Worker with 12 years of experience[^<]*', bio),
    ('View full bio', 'Read our editorial policy'),
    (r'>\s*Sarah Chen\s*<', '>DTS Research Team<'),
]

total_files = 0
for html_path in glob.glob(os.path.join(OUT, '*.html')):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    original = html
    for pattern, replacement in replacements:
        html = re.sub(pattern, replacement, html)
    if html != original:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
        total_files += 1
print(f'Output HTML: {total_files} files updated')

tmp_count = 0
for tmp_path in glob.glob(os.path.join(BASE, 'tmp_build_*.py')):
    with open(tmp_path, 'r', encoding='utf-8') as f:
        tmp = f.read()
    original = tmp
    for pattern, replacement in replacements:
        tmp = re.sub(pattern, replacement, tmp)
    if tmp != original:
        with open(tmp_path, 'w', encoding='utf-8') as f:
            f.write(tmp)
        tmp_count += 1
print(f'tmp_build scripts: {tmp_count} files updated')

alt_bp = os.path.join(OUT, 'assets', 'build_pages.py')
if os.path.exists(alt_bp):
    with open(alt_bp, 'r', encoding='utf-8') as f:
        alt = f.read()
    original = alt
    alt = re.sub(r"'reviewer_bio':\s*['\"]Dr\. Chen is[^'\"]*['\"]", f"'reviewer_bio': '{bio}'", alt)
    for pattern, replacement in replacements:
        alt = re.sub(pattern, replacement, alt)
    if alt != original:
        with open(alt_bp, 'w', encoding='utf-8') as f:
            f.write(alt)
        print('output/assets/build_pages.py: updated')

print('\n--- VERIFICATION ---')
remaining = 0
for html_path in glob.glob(os.path.join(OUT, '*.html')):
    with open(html_path, 'r', encoding='utf-8') as f:
        c = f.read()
        if 'Sarah Chen' in c or 'Dr. Chen' in c:
            remaining += 1
            print(f'  REMAINING: {os.path.basename(html_path)}')

for py_path in glob.glob(os.path.join(BASE, '*.py')):
    with open(py_path, 'r', encoding='utf-8') as f:
        c = f.read()
        if 'Sarah Chen' in c or 'Dr. Chen' in c:
            bn = os.path.basename(py_path)
            if bn != 'fix_reviewer.py':
                remaining += 1
                print(f'  REMAINING: {bn}')

print(f'\nTotal files still containing Sarah Chen/Dr. Chen: {remaining}')
print('DONE')
