"""Quality gate for PS-CONDITIONS-01."""
import os
import re
import sys

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

OUTPUT = r'D:\Work\Digital-Therapy-Solutions\output'

REQUIRED_SLUGS = [
    'ocd', 'ptsd', 'bipolar', 'eating-disorders', 'grief',
    'anger', 'addiction', 'stress', 'relationship', 'lgbtq',
    'teen', 'postpartum', 'burnout', 'insomnia', 'chronic-pain',
    'social-anxiety', 'phobias', 'panic', 'loneliness', 'self-esteem',
]

REQUIRED_NAV = [
    'href="index.html"',
    'href="conditions.html"',
    'href="reviews.html"',
    'href="insurance.html"',
    'href="about.html"',
]

errors = []
warnings = []

print("=== PS-CONDITIONS-01 Quality Gate ===\n")

# 1. Check all 20 files exist
print("1. File existence check:")
for slug in REQUIRED_SLUGS:
    path = os.path.join(OUTPUT, slug + '.html')
    if os.path.exists(path):
        print(f"   OK  {slug}.html")
    else:
        print(f"   MISS {slug}.html")
        errors.append(f"Missing file: {slug}.html")

# 2. Content checks all 20 pages
print("\n2. Content checks (all 20 pages):")
for slug in REQUIRED_SLUGS:
    path = os.path.join(OUTPUT, slug + '.html')
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    page_errors = []
    
    if '{{' in html and '}}' in html:
        page_errors.append("Contains {{}} placeholder")
    
    for nav_href in REQUIRED_NAV:
        if nav_href not in html:
            page_errors.append(f"Missing nav: {nav_href}")
    
    if 'breadcrumb' not in html:
        page_errors.append("Missing breadcrumb")
    
    card_count = html.count('platform-card__name')
    if card_count < 3:
        page_errors.append(f"Only {card_count} platform cards")
    
    if 'comparison-table' not in html:
        page_errors.append("Missing comparison table")
    
    if 'forks-section' not in html:
        page_errors.append("Missing forks section")
    
    if 'reviewer-card' not in html:
        page_errors.append("Missing reviewer card")
    
    if 'site-footer' not in html:
        page_errors.append("Missing footer")
    
    if 'IntersectionObserver' not in html:
        page_errors.append("Missing JS block")
    
    meta = re.search(r'<meta name="description" content="([^"]+)"', html)
    if not meta:
        page_errors.append("Missing meta description")
    else:
        desc_len = len(meta.group(1))
        if desc_len < 130 or desc_len > 165:
            warnings.append(f"{slug}: meta desc length {desc_len}")
    
    if 'rating-badge--top' not in html:
        page_errors.append("Missing Top Rated badge")
    
    if page_errors:
        for e in page_errors:
            print(f"   FAIL {slug}.html: {e}")
            errors.append(f"{slug}.html: {e}")
    else:
        print(f"   PASS {slug}.html")

# 3. Conditions.html check
print("\n3. conditions.html check:")
conditions_path = os.path.join(OUTPUT, 'conditions.html')
with open(conditions_path, 'r', encoding='utf-8') as f:
    chtml = f.read()

stubs = chtml.count('hub-card--stub')
live_hrefs = re.findall(r'href="([^"]+)" class="hub-card__cta"', chtml)
print(f"   Live cards: {len(live_hrefs)}")
print(f"   Remaining stubs: {stubs}")

sprint_pages = [s + '.html' for s in REQUIRED_SLUGS]
missing_links = []
for sp in sprint_pages:
    if sp not in live_hrefs:
        missing_links.append(sp)
        errors.append(f"conditions.html missing link to {sp}")

if missing_links:
    print(f"   FAIL missing links: {missing_links}")
else:
    print(f"   PASS all 20 sprint pages linked")

# 4. Summary
print(f"\n=== SUMMARY ===")
print(f"Files in output/: {len(os.listdir(OUTPUT))}")
if errors:
    print(f"FAILED -- {len(errors)} error(s):")
    for e in errors:
        print(f"   - {e}")
else:
    print(f"ALL CHECKS PASSED")

if warnings:
    print(f"\nWARNINGS ({len(warnings)}):")
    for w in warnings:
        print(f"   - {w}")
