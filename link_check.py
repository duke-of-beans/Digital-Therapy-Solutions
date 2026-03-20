import os, re
from urllib.parse import urlparse

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

html_files = [f for f in os.listdir(output_dir) if f.endswith('.html')]
all_pages = set(html_files)

dead_links = []
checked = 0

for fname in sorted(html_files):
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all href= values
    hrefs = re.findall(r'href="([^"]+)"', content)

    for href in hrefs:
        # Skip: tel:, sms:, mailto:, #anchors, external http, empty
        if not href or href.startswith('#') or href.startswith('tel:') or \
           href.startswith('sms:') or href.startswith('mailto:') or \
           href.startswith('http') or href.startswith('//'):
            continue

        # Normalize: strip fragment
        clean = href.split('#')[0]
        if not clean:
            continue

        # Internal .html link
        if clean.endswith('.html'):
            # Must exist in output/
            target_name = os.path.basename(clean)
            if target_name not in all_pages:
                dead_links.append(f'  [{fname}] → {href} (FILE NOT FOUND: {target_name})')
            checked += 1
        elif clean.startswith('../') or clean.startswith('./'):
            # Relative non-html (CSS, assets) — skip for now
            pass
        elif clean.startswith('/'):
            # Absolute paths — these are dead
            dead_links.append(f'  [{fname}] → {href} (ABSOLUTE PATH — should be relative)')

print(f'Checked {checked} internal .html links across {len(html_files)} files')
print()
if dead_links:
    print(f'DEAD LINKS ({len(dead_links)}):')
    for d in sorted(dead_links):
        print(d)
else:
    print('NO DEAD LINKS — all internal .html links resolve correctly')

# Also check for remaining absolute /path links
print()
print('Checking for remaining absolute nav/footer links...')
absolute_found = []
for fname in sorted(html_files):
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Look for href="/" or href="/something" that isn't http
    abs_hrefs = re.findall(r'href="(/[^/"#][^"]*)"', content)
    for h in abs_hrefs:
        absolute_found.append(f'  [{fname}] → {h}')

if absolute_found:
    print(f'ABSOLUTE LINKS REMAINING ({len(absolute_found)}):')
    for a in sorted(set(absolute_found)):
        print(a)
else:
    print('No absolute /path links found — all clean')

# Count pages
print()
print(f'Total pages in output/: {len(html_files)}')
for f in sorted(html_files):
    size = os.path.getsize(os.path.join(output_dir, f))
    print(f'  {f} ({size:,} bytes)')
