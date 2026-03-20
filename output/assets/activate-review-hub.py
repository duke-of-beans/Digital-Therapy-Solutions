import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

reviews_html = Path(r'D:\Work\Digital-Therapy-Solutions\output\reviews.html')
html = reviews_html.read_text(encoding='utf-8')

# Map: slug -> (display_name, best_for_short)
# Derive from the hub cards already in the file - we just need to:
# 1. Remove hub-card--stub class
# 2. Change <span class="hub-card__cta">Coming Soon</span> -> <a class="hub-card__cta" href="[slug]-review.html">Read Review ->
PLATFORMS = [
    'adhd-online', 'amwell', 'bend-health', 'brightline', 'brightside',
    'calmerry', 'cerebral', 'circle-medical', 'doctor-on-demand', 'done-adhd',
    'faithful-counseling', 'gay-therapy-center', 'grow-therapy', 'headspace', 'headway',
    'inclusive-therapists', 'klarity', 'lunajoy', 'manatee-health', 'mindful-care',
    'nocd', 'open-path', 'our-relationship', 'our-ritual', 'pride-counseling',
    'psychology-today', 'regain', 'simplepractice', 'talkiatry', 'teen-counseling',
    'therapyden'
]

# Remove hub-card--stub from all stub cards
html = html.replace(' hub-card--stub', '')
# Remove section-context "3 full reviews live" line
html = re.sub(
    r'<p class="section-context">[^<]*</p>\s*',
    '<p class="section-context">34 full reviews live. Updated monthly.</p>\n',
    html,
    count=1
)
# Replace all <span class="hub-card__cta">Coming Soon</span> with anchors
# We need to match each to its slug — do it by processing surrounding card context
# Strategy: replace stub span CTAs with read review links, using data from logo src attr
# The logo src is ../assets/logos/[slug].webp — extract slug from that
def replace_stub(m):
    card_html = m.group(0)
    # Find slug from logo src
    slug_match = re.search(r'logos/([^.]+)\.webp', card_html)
    if not slug_match:
        return card_html
    slug = slug_match.group(1)
    # Replace the span CTA with an anchor
    card_html = re.sub(
        r'<span class="hub-card__cta">Coming Soon</span>',
        f'<a class="hub-card__cta" href="{slug}-review.html">Read Review &#x2192;</a>',
        card_html
    )
    return card_html

# Match each hub-card div (was stub, now class removed) that still has a span CTA
html = re.sub(
    r'<div class="hub-card">\s*<img[^>]+logos/[^>]+>[\s\S]*?<span class="hub-card__cta">Coming Soon</span>\s*</div>',
    replace_stub,
    html
)

reviews_html.write_text(html, encoding='utf-8')

# Verify
remaining = html.count('<span class="hub-card__cta">Coming Soon</span>')
live = html.count('<a class="hub-card__cta"')
print(f'Done. Live cards: {live}, Remaining stubs: {remaining}')
