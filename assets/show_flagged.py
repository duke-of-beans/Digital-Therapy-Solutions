import sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup
flagged = [
    'anger.html','autism.html','beacon.html','betterhelp-review.html',
    'centene.html','chip.html','chronic-pain.html','harvard-pilgrim.html',
    'highmark.html','kaiser.html','life-transitions.html','magellan.html',
    'medicare.html','mens-mental-health.html','online-therapy-com-review.html',
    'panic.html','phobias.html','privacy-policy.html','relationship.html',
    'social-anxiety.html','tricare.html','tufts.html','womens-mental-health.html'
]
for fn in flagged:
    f = pathlib.Path('output') / fn
    soup = BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser')
    tag = soup.find('meta', {'name': 'description'})
    desc = tag['content'].strip() if tag and tag.get('content') else 'MISSING'
    print(f"{fn}: [{len(desc)}] {desc}")
