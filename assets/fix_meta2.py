import sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

FIXES2 = {
    'autism.html':
        'Best online therapy for autism and neurodivergence. Expert-reviewed, neurodiversity-affirming platforms. Real pricing and insurance options. Updated 2026.',
    'centene.html':
        'Does Centene cover online therapy? See what Centene Medicaid and Marketplace plans cover, which platforms work, and how to access care. Updated 2026.',
    'harvard-pilgrim.html':
        'Does Harvard Pilgrim cover online therapy? Compare in-network platforms, expected copays, and how to access telehealth mental health benefits. Updated 2026.',
    'kaiser.html':
        'Does Kaiser cover online therapy? See what\'s covered, which platforms work with Kaiser, and how to access telehealth mental health care. Updated 2026.',
    'life-transitions.html':
        'Best online therapy for life transitions. Expert-reviewed platforms with therapists in adjustment, grief, and navigating major change. Updated 2026.',
    'medicare.html':
        'Does Medicare cover online therapy? Yes — Part B covers telehealth therapy. Compare covered platforms, copay estimates, and how to access care. Updated 2026.',
    'tricare.html':
        'Does Tricare cover online therapy? Yes. Compare covered platforms, copay expectations, and how military families can access mental health care. Updated 2026.',
    'tufts.html':
        'Does Tufts Health Plan cover online therapy? Compare in-network platforms, expected copays, and how to access telehealth mental health benefits. Updated 2026.',
}

OUTPUT_DIR = pathlib.Path('output')
for filename, new_desc in FIXES2.items():
    f = OUTPUT_DIR / filename
    n = len(new_desc)
    content = f.read_text(encoding='utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    tag = soup.find('meta', {'name': 'description'})
    if tag:
        tag['content'] = new_desc
    f.write_text(str(soup), encoding='utf-8')
    status = 'PASS' if 120 <= n <= 160 else 'WARN'
    print(f"{status} [{n}]: {filename}")
print("Done.")
