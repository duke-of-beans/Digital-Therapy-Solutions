import pathlib, sys, re
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')

files_to_fix = [
    'D:/Work/Digital-Therapy-Solutions/output/affordable.html',
]

# Also scan all pages for .logo with background-color inline style
import os
output_dir = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output')
all_html = list(output_dir.glob('*.html'))

fixed_total = 0
for fpath in all_html:
    html = fpath.read_text(encoding='utf-8')
    if 'class="logo"' not in html and "class='logo'" not in html:
        continue
    soup = BeautifulSoup(html, 'html.parser')
    changed = False
    for div in soup.find_all('div', class_='logo'):
        # Replace colored bg with --bg-secondary, add size constraints
        div['style'] = 'width:64px;height:64px;min-width:64px;min-height:64px;background-color:var(--bg-secondary);border-radius:8px;display:flex;align-items:center;justify-content:center;overflow:hidden;'
        img = div.find('img')
        if img:
            img['style'] = 'width:56px;height:56px;object-fit:contain;display:block;'
        changed = True
        fixed_total += 1
    if changed:
        fpath.write_text(str(soup), encoding='utf-8')
        print(f"Fixed {fpath.name}")

print(f"Total logo wrappers fixed: {fixed_total}")
