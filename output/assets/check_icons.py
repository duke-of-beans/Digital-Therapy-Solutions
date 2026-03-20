import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
pages = [p for p in os.listdir('output') if p.endswith('.html')]
emoji_pages = []
icon_pages = []
for p in pages:
    with open(f'output/{p}', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    if re.search(r'[\U0001F300-\U0001FFFF]|[\U00002600-\U000027FF]|\u2714|\u2716|\u2728|\u2705|\u274C', content):
        emoji_pages.append(p)
    if 'condition-tile__icon' in content or 'hub-card' in content:
        if '<svg' in content:
            icon_pages.append(p)
print('EMOJI PAGES:', emoji_pages if emoji_pages else 'None')
print('SVG ICON PAGES:', icon_pages[:10])
print('Total pages with hub-card SVGs:', len(icon_pages))
