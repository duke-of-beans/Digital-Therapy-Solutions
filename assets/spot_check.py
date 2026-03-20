import sys, pathlib, json
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

OUTPUT_DIR = pathlib.Path('output')

checks = [
    ('anxiety.html', ['canonical', 'BreadcrumbList', 'FAQPage']),
    ('betterhelp-review.html', ['canonical', 'BreadcrumbList', 'Review']),
    ('aetna.html', ['canonical', 'BreadcrumbList', 'FAQPage']),
    ('index.html', ['canonical', 'BreadcrumbList']),
]

all_pass = True
for filename, expected in checks:
    f = OUTPUT_DIR / filename
    soup = BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser')

    # canonical
    canon = soup.find('link', {'rel': 'canonical'})
    has_canon = bool(canon)

    # JSON-LD types
    schemas_found = []
    for s in soup.find_all('script', {'type': 'application/ld+json'}):
        if s.string:
            try:
                data = json.loads(s.string)
                schemas_found.append(data.get('@type', ''))
            except:
                pass

    print(f"\n--- {filename} ---")
    for check in expected:
        if check == 'canonical':
            ok = has_canon
            print(f"  {'PASS' if ok else 'FAIL'} canonical: {canon['href'] if canon else 'MISSING'}")
        else:
            ok = any(check in t for t in schemas_found)
            print(f"  {'PASS' if ok else 'FAIL'} {check} schema")
        if not ok:
            all_pass = False

# Check sitemap.xml
sitemap = OUTPUT_DIR / 'sitemap.xml'
print(f"\n--- sitemap.xml ---")
if sitemap.exists():
    content = sitemap.read_text(encoding='utf-8')
    url_count = content.count('<url>')
    print(f"  PASS exists, {url_count} <url> entries")
    if not content.startswith('<?xml'):
        print('  FAIL: missing XML declaration')
        all_pass = False
else:
    print('  FAIL: not found')
    all_pass = False

# Check robots.txt
robots = OUTPUT_DIR / 'robots.txt'
print(f"\n--- robots.txt ---")
if robots.exists():
    content = robots.read_text(encoding='utf-8')
    has_allow = 'Allow: /' in content
    has_sitemap = 'Sitemap:' in content
    print(f"  {'PASS' if has_allow else 'FAIL'} Allow: /")
    print(f"  {'PASS' if has_sitemap else 'FAIL'} Sitemap directive")
else:
    print('  FAIL: not found')
    all_pass = False

print(f"\n{'ALL SPOT CHECKS PASSED' if all_pass else 'SOME SPOT CHECKS FAILED'}")
