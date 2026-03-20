import sys, pathlib, re
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

OUTPUT_DIR = pathlib.Path('output')

# Nav/footer tags to exclude — links inside these don't count as body content links
NAV_SELECTORS = ['nav', 'footer', '.site-nav', '.site-footer', '.breadcrumb']

def get_body_internal_links(soup):
    """Count internal links in body content, excluding nav/footer."""
    # Remove nav and footer elements from consideration
    working = BeautifulSoup(str(soup), 'html.parser')
    for sel in NAV_SELECTORS:
        for el in working.select(sel):
            el.decompose()
    # Also remove script/style
    for el in working.find_all(['script','style']):
        el.decompose()

    links = working.find_all('a', href=True)
    internal = []
    for a in links:
        href = a['href']
        # Internal: points to a .html file (relative), not an external URL
        if href.startswith('http://') or href.startswith('https://') or href.startswith('mailto:') or href.startswith('#'):
            continue
        if href.endswith('.html') or re.match(r'^[a-z0-9\-]+\.html', href):
            internal.append(href)
    return internal

html_files = sorted(OUTPUT_DIR.glob('*.html'))
results = []

for f in html_files:
    content = f.read_text(encoding='utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    links = get_body_internal_links(soup)
    count = len(links)
    status = 'PASS' if count >= 3 else 'FLAG'
    results.append((f.name, count, status, links))

lines = ['# INTERNAL_LINKS_AUDIT.md\n\n',
         f'Generated: 2026-03-20 | Pages: {len(results)}\n\n',
         '| File | Body Links | Status | Links Found |\n',
         '|---|---|---|---|\n']

flagged = []
for name, count, status, links in results:
    link_str = ', '.join(links[:8]) + ('...' if len(links) > 8 else '')
    lines.append(f'| {name} | {count} | {status} | {link_str} |\n')
    if status == 'FLAG':
        flagged.append((name, count, links))

summary_pass = sum(1 for _, _, s, _ in results if s == 'PASS')
summary_flag = sum(1 for _, _, s, _ in results if s == 'FLAG')
lines.append(f'\n## Summary\n- PASS (>=3 body links): {summary_pass}\n- FLAG (<3 body links): {summary_flag}\n')
if flagged:
    lines.append('\n## Flagged Pages\n')
    for name, count, links in flagged:
        lines.append(f'- **{name}**: {count} body link(s)\n')

out = pathlib.Path('INTERNAL_LINKS_AUDIT.md')
out.write_text(''.join(lines), encoding='utf-8')
print('INTERNAL_LINKS_AUDIT.md written.')
print(f'PASS: {summary_pass} | FLAG: {summary_flag}')
print('\nFlagged pages (worst offenders):')
for name, count, links in sorted(flagged, key=lambda x: x[1]):
    print(f'  [{count}] {name}')
