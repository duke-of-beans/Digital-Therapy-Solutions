"""Pass 2: Fix remaining 6 files with variant HTML patterns."""
import re, os, glob

OUT = r'D:\Work\Digital-Therapy-Solutions\output'
bio = 'Every recommendation on this page was independently researched, cross-referenced against current clinical literature, and verified for accuracy by the DTS editorial team. Platforms are re-evaluated monthly.'

replacements_p2 = [
    # Bio wrapped in <p> tags
    (r'<p>Dr\. Chen is a Licensed Clinical Social Worker[^<]*</p>', f'<p>{bio}</p>'),
    # Bare "Sarah Chen" text (with possible whitespace)
    (r'Sarah Chen', 'DTS Research Team'),
    # Any remaining "Dr. Chen" references
    (r'Dr\. Chen', 'the DTS editorial team'),
]

fixed = 0
for html_path in glob.glob(os.path.join(OUT, '*.html')):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    original = html
    for pattern, replacement in replacements_p2:
        html = re.sub(pattern, replacement, html)
    if html != original:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
        fixed += 1
        print(f'  Fixed: {os.path.basename(html_path)}')

print(f'\nPass 2: {fixed} files updated')

# Final verification
print('\n--- FINAL VERIFICATION ---')
remaining = 0
for html_path in glob.glob(os.path.join(OUT, '*.html')):
    with open(html_path, 'r', encoding='utf-8') as f:
        c = f.read()
        if 'Sarah Chen' in c or 'Dr. Chen' in c:
            remaining += 1
            # Find the line
            for i, line in enumerate(c.split('\n'), 1):
                if 'Sarah Chen' in line or 'Dr. Chen' in line:
                    print(f'  STILL: {os.path.basename(html_path)}:{i} -> {line.strip()[:80]}')
                    break

# Also check build_pages.py and tmp files
BASE = r'D:\Work\Digital-Therapy-Solutions'
for py_path in glob.glob(os.path.join(BASE, '*.py')):
    bn = os.path.basename(py_path)
    if bn in ('fix_reviewer.py', 'fix_reviewer_p2.py'):
        continue
    with open(py_path, 'r', encoding='utf-8') as f:
        c = f.read()
        if 'Sarah Chen' in c or 'Dr. Chen' in c:
            remaining += 1
            print(f'  STILL: {bn}')

print(f'\nTotal files still containing Sarah Chen/Dr. Chen: {remaining}')
if remaining == 0:
    print('ALL CLEAR - Zero references remain.')
print('DONE')
