import re
with open('output/conditions.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all hub-card__name values
all_cards = re.findall(r'hub-card__name\">(.*?)</div>', html)
print(f"All cards ({len(all_cards)}):")
for c in all_cards:
    is_stub = False
    # Check context
    print(f"  {c.strip()}")

# Count live vs stub
live = html.count('class="hub-card"')
stub = html.count('hub-card--stub')
print(f"\nLive (hub-card without stub): {live}")
print(f"Stub (hub-card--stub): {stub}")

# Check specific pages
for slug in ['burnout.html', 'social-anxiety.html', 'phobias.html', 'panic.html']:
    if slug in html:
        print(f"  FOUND link to {slug}")
    else:
        print(f"  MISSING link to {slug}")
