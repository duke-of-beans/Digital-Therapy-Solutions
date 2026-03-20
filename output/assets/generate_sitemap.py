import sys, pathlib
from datetime import date
sys.stdout.reconfigure(encoding='utf-8')

DOMAIN = 'https://digitaltherapysolutions.com'
TODAY = date.today().isoformat()
OUTPUT_DIR = pathlib.Path('output')

# Priority tiers
HUB_PAGES = {'reviews.html', 'conditions.html', 'insurance.html'}
CONDITION_PAGES = {
    'anxiety.html','depression.html','adhd.html','couples.html','ocd.html',
    'ptsd.html','bipolar.html','eating-disorders.html','grief.html','anger.html',
    'addiction.html','stress.html','burnout.html','relationship.html','lgbtq.html',
    'teen.html','postpartum.html','insomnia.html','chronic-pain.html',
    'social-anxiety.html','phobias.html','panic.html','loneliness.html',
    'self-esteem.html','mens-mental-health.html','womens-mental-health.html',
    'life-transitions.html','autism.html',
}
INSURANCE_PAGES = {
    'aetna.html','bcbs.html','cigna.html','unitedhealthcare.html','medicaid.html',
    'affordable.html','humana.html','kaiser.html','anthem.html','molina.html',
    'oscar.html','ambetter.html','wellcare.html','tricare.html','chip.html',
    'medicare.html','beacon.html','magellan.html','centene.html','highmark.html',
    'harvard-pilgrim.html','tufts.html','community-health.html',
}
REVIEW_PAGES = {
    'betterhelp-review.html','talkspace-review.html','online-therapy-com-review.html',
}
LEGAL_PAGES = {'privacy-policy.html','affiliate-disclosure.html','editorial-policy.html'}
SUPPORTING_PAGES = {
    'about.html','how-online-therapy-works.html','do-i-need-therapy.html','crisis-resources.html'
}

def get_priority(fn):
    if fn == 'index.html': return '1.0'
    if fn in HUB_PAGES: return '0.9'
    if fn in CONDITION_PAGES: return '0.8'
    if fn in INSURANCE_PAGES: return '0.8'
    if fn in REVIEW_PAGES: return '0.8'
    if fn in SUPPORTING_PAGES: return '0.6'
    if fn in LEGAL_PAGES: return '0.4'
    return '0.5'

def get_url(fn):
    if fn == 'index.html':
        return f'{DOMAIN}/'
    return f'{DOMAIN}/{fn.replace(".html", "")}'

html_files = sorted(OUTPUT_DIR.glob('*.html'))

lines = ['<?xml version="1.0" encoding="UTF-8"?>\n']
lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

# index.html first
for f in html_files:
    if f.name == 'index.html':
        lines.append(f'  <url>\n')
        lines.append(f'    <loc>{get_url(f.name)}</loc>\n')
        lines.append(f'    <lastmod>{TODAY}</lastmod>\n')
        lines.append(f'    <changefreq>monthly</changefreq>\n')
        lines.append(f'    <priority>{get_priority(f.name)}</priority>\n')
        lines.append(f'  </url>\n')

# Hub pages next, then all others
order = []
for f in html_files:
    if f.name != 'index.html':
        order.append(f)

for f in order:
    lines.append(f'  <url>\n')
    lines.append(f'    <loc>{get_url(f.name)}</loc>\n')
    lines.append(f'    <lastmod>{TODAY}</lastmod>\n')
    lines.append(f'    <changefreq>monthly</changefreq>\n')
    lines.append(f'    <priority>{get_priority(f.name)}</priority>\n')
    lines.append(f'  </url>\n')

lines.append('</urlset>\n')

out = OUTPUT_DIR / 'sitemap.xml'
out.write_text(''.join(lines), encoding='utf-8')
print(f"sitemap.xml written with {len(html_files)} URLs.")
print(f"Path: {out}")
