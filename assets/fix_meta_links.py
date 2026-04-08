import os, re

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

# Find all remaining href="#" inside platform-card__meta (the "See full review" links)
# These should point to the actual review page for each platform
# Pattern: <a href="#">See full review →</a> inside platform-card__meta

count = 0
for fname in os.listdir(output_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find platform-card__meta blocks with href="#" and extract data-platform from nearby cta-button
    # Strategy: find each platform-card block, extract data-platform, fix the meta link href
    def fix_meta_links(html):
        # For each platform-card, find data-platform and fix the meta See full review link
        pattern = re.compile(
            r'(data-platform="([^"]+)"[^<]*(?:<[^>]*>)*?.*?)'
            r'(<div class="platform-card__meta">.*?<a href="#">)(See full review)',
            re.DOTALL
        )
        def replacer(m):
            platform_slug = m.group(2)
            review_href = f'{platform_slug}-review.html'
            return m.group(1) + m.group(3).replace('href="#"', f'href="{review_href}"') + m.group(4)
        return pattern.sub(replacer, html)

    new_content = fix_meta_links(content)
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f'Platform meta review links fixed on {count} pages')
