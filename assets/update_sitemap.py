import os, re
from datetime import date

sitemap_path = r'D:\Work\Digital-Therapy-Solutions\output\sitemap.xml'
today = date.today().isoformat()  # 2026-04-08

with open(sitemap_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update all lastmod dates to today
content = re.sub(r'<lastmod>[^<]+</lastmod>', f'<lastmod>{today}</lastmod>', content)

# Remove the 404 URL block entirely
content = re.sub(
    r'\s*<url>\s*<loc>https://digitaltherapysolutions\.com/404</loc>.*?</url>',
    '',
    content,
    flags=re.DOTALL
)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Count URLs
url_count = content.count('<loc>')
print(f'Sitemap updated: {url_count} URLs, lastmod={today}, 404 removed')
