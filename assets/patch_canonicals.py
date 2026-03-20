import sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

OUTPUT_DIR = pathlib.Path('output')
DOMAIN = 'https://digitaltherapysolutions.com'

def canonical_url(filename):
    if filename == 'index.html':
        return f'{DOMAIN}/'
    stem = filename.replace('.html', '')
    return f'{DOMAIN}/{stem}'

html_files = sorted(OUTPUT_DIR.glob('*.html'))
added = 0
already = 0

for f in html_files:
    content = f.read_text(encoding='utf-8')
    soup = BeautifulSoup(content, 'html.parser')

    # Check if canonical already exists
    existing = soup.find('link', {'rel': 'canonical'})
    if existing:
        already += 1
        print(f"ALREADY PRESENT: {f.name}")
        continue

    url = canonical_url(f.name)
    canon_tag = soup.new_tag('link', rel='canonical', href=url)

    # Insert after last <meta> in <head>
    head = soup.head
    metas = head.find_all('meta') if head else []
    if metas:
        metas[-1].insert_after(canon_tag)
    elif head:
        head.append(canon_tag)
    else:
        print(f"WARNING: no <head> in {f.name}")
        continue

    f.write_text(str(soup), encoding='utf-8')
    added += 1
    print(f"ADDED: {f.name} -> {url}")

print(f"\nDone. Added: {added}, Already present: {already}")
