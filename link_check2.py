import os, re
import sys

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

html_files = [f for f in os.listdir(output_dir) if f.endswith('.html')]
all_pages = set(html_files)

dead_links = []
checked = 0

for fname in sorted(html_files):
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    hrefs = re.findall(r'href="([^"]+)"', content)

    for href in hrefs:
        if not href or href.startswith('#') or href.startswith('tel:') or \
           href.startswith('sms:') or href.startswith('mailto:') or \
           href.startswith('http') or href.startswith('//'):
            continue

        clean = href.split('#')[0]
        if not clean:
            continue

        if clean.endswith('.html'):
            target_name = os.path.basename(clean)
            if target_name not in all_pages:
                dead_links.append(f'  [{fname}] -> {href} (FILE NOT FOUND: {target_name})')
            checked += 1
        elif clean.startswith('/'):
            dead_links.append(f'  [{fname}] -> {href} (ABSOLUTE PATH)')

print(f'Checked {checked} internal .html links across {len(html_files)} files')
print()
if dead_links:
    print(f'DEAD LINKS ({len(dead_links)}):')
    for d in sorted(dead_links):
        print(d)
else:
    print('NO DEAD LINKS -- all internal .html links resolve correctly')

# Check for remaining absolute /path links
print()
absolute_found = []
for fname in sorted(html_files):
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    abs_hrefs = re.findall(r'href="(/[^/"#h][^"]*)"', content)
    for h in abs_hrefs:
        absolute_found.append(f'  [{fname}] -> {h}')

if absolute_found:
    print(f'ABSOLUTE LINKS REMAINING ({len(absolute_found)}):')
    for a in sorted(set(absolute_found)):
        print(a)
else:
    print('No absolute /path links found -- all clean')

print()
print(f'Total pages: {len(html_files)}')
for f in sorted(html_files):
    size = os.path.getsize(os.path.join(output_dir, f))
    print(f'  {f} ({size:,} bytes)')
