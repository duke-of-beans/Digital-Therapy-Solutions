import re
with open('output/conditions.html', 'r', encoding='utf-8') as f:
    html = f.read()
stubs = re.findall(r'hub-card--stub.*?hub-card__name\">(.*?)</div>', html, re.DOTALL)
print(f"Remaining stubs ({len(stubs)}):")
for s in stubs:
    print(' ', repr(s.strip()))
