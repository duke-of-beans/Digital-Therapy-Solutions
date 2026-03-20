import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')

output = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output')
pages = list(output.glob('*.html'))

revealed_pages = []
visible_pages = []
neither = []

for p in pages:
    html = p.read_text(encoding='utf-8', errors='ignore')
    if "classList.add('revealed')" in html:
        revealed_pages.append(p.name)
    elif "classList.add('visible')" in html:
        visible_pages.append(p.name)
    else:
        neither.append(p.name)

print(f"Using 'revealed' (BROKEN): {len(revealed_pages)}")
for n in revealed_pages[:5]: print(f"  {n}")
print(f"  ... and {len(revealed_pages)-5} more" if len(revealed_pages) > 5 else "")
print(f"\nUsing 'visible' (CORRECT): {len(visible_pages)}")
print(f"Neither: {len(neither)}")

# Fix all broken pages
fixed = 0
for p in pages:
    html = p.read_text(encoding='utf-8', errors='ignore')
    if "classList.add('revealed')" in html:
        new_html = html.replace("classList.add('revealed')", "classList.add('visible')")
        p.write_text(new_html, encoding='utf-8')
        fixed += 1

print(f"\nFixed: {fixed} pages")
