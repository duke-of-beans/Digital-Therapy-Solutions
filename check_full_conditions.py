import re
with open('output/conditions.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all anchor hrefs in hub-card context
hrefs = re.findall(r'href="([^"]+)" class="hub-card__cta"', html)
print("Live card hrefs:")
for h in hrefs:
    print(f"  {h}")

# Count all hub-card sections
print(f"\nTotal hub-card__name entries: {html.count('hub-card__name')}")
print(f"hub-card--stub entries: {html.count('hub-card--stub')}")

# The sprint requires burnout, social-anxiety, phobias, panic to be linked
# Check if there are stub cards for them at all
for term in ['Burnout', 'Social Anxiety', 'Phobia', 'Panic', 'Stress']:
    idx = html.find(term)
    if idx >= 0:
        snippet = html[max(0,idx-100):idx+80]
        print(f"\n--- {term} context ---")
        print(snippet)
