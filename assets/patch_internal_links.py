import sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

# Related guides block per page — 3 contextually relevant links each
RELATED = {
    'privacy-policy.html': {
        'title': 'Also worth reading',
        'links': [
            ('How Online Therapy Works', 'how-online-therapy-works.html'),
            ('Our Editorial Policy', 'editorial-policy.html'),
            ('Affiliate Disclosure', 'affiliate-disclosure.html'),
        ]
    },
    'about.html': {
        'title': 'Also worth reading',
        'links': [
            ('How Online Therapy Works', 'how-online-therapy-works.html'),
            ('Our Editorial Policy', 'editorial-policy.html'),
            ('Browse All Platform Reviews', 'reviews.html'),
        ]
    },
    'affiliate-disclosure.html': {
        'title': 'Also worth reading',
        'links': [
            ('Our Editorial Policy', 'editorial-policy.html'),
            ('About Digital Therapy Solutions', 'about.html'),
            ('Privacy Policy', 'privacy-policy.html'),
        ]
    },
    'editorial-policy.html': {
        'title': 'Also worth reading',
        'links': [
            ('Affiliate Disclosure', 'affiliate-disclosure.html'),
            ('About Digital Therapy Solutions', 'about.html'),
            ('Browse All Platform Reviews', 'reviews.html'),
        ]
    },
}

SECTION_HTML = """
<div class="section-wrapper" style="padding:var(--space-xl) var(--space-md);max-width:var(--table-width);margin:0 auto;">
  <h2 style="font-family:var(--font-serif);font-size:1.4rem;margin-bottom:var(--space-md);">{title}</h2>
  <ul style="list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:var(--space-sm);">
    {items}
  </ul>
</div>
"""
ITEM_HTML = '<li><a href="{href}" style="color:var(--accent-primary);text-decoration:underline;">{text}</a></li>'

OUTPUT_DIR = pathlib.Path('output')

for filename, data in RELATED.items():
    f = OUTPUT_DIR / filename
    if not f.exists():
        print(f"NOT FOUND: {filename}")
        continue
    content = f.read_text(encoding='utf-8')
    soup = BeautifulSoup(content, 'html.parser')

    footer = soup.find('footer')
    if not footer:
        print(f"NO FOOTER: {filename} — skipping")
        continue

    items_html = '\n    '.join(
        ITEM_HTML.format(href=href, text=text)
        for text, href in data['links']
    )
    section_html = SECTION_HTML.format(title=data['title'], items=items_html)
    section_soup = BeautifulSoup(section_html, 'html.parser')

    footer.insert_before(section_soup)
    f.write_text(str(soup), encoding='utf-8')
    print(f"PATCHED: {filename} (+{len(data['links'])} links)")

print("Done.")
