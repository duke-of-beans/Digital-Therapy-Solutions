import sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

# Optimized meta descriptions for all flagged pages (120-160 chars)
FIXES = {
    # LONG -> trimmed tight
    'anger.html':
        'Best online therapy for anger management. Expert-reviewed platforms using CBT and evidence-based approaches. Real pricing, insurance details. Updated 2026.',
    'autism.html':
        'Find online therapy for autism and neurodivergence. Expert-reviewed platforms with neurodiversity-affirming therapists. Real pricing and insurance options. Updated 2026.',
    'beacon.html':
        'Does Beacon Health Options cover online therapy? See how Beacon behavioral health coverage works and which platforms are in-network. Updated 2026.',
    'betterhelp-review.html':
        'BetterHelp review 2026: honest pros, cons, and real pricing ($65-100/week). Tested by our team. Find out who it\'s best for and who should look elsewhere.',
    'centene.html':
        'Does Centene cover online therapy? See what\'s covered through Centene Medicaid and Marketplace plans, which platforms work, and how to access care. Updated 2026.',
    'chip.html':
        'Does CHIP cover online therapy for children? Yes, in most states. See what mental health services are covered and how to access telehealth care. Updated 2026.',
    'chronic-pain.html':
        'Best online therapy for chronic pain. Expert-reviewed platforms for mental health support with long-term conditions. Insurance coverage included. Updated 2026.',
    'harvard-pilgrim.html':
        'Does Harvard Pilgrim cover online therapy? Yes. Compare in-network platforms, expected copays, and how to access telehealth mental health benefits. Updated 2026.',
    'highmark.html':
        'Does Highmark cover online therapy? Yes. Highmark BCBS covers telehealth therapy in PA, WV, and DE. Compare platforms and copay estimates. Updated 2026.',
    'kaiser.html':
        'Does Kaiser Permanente cover online therapy? See what\'s covered, which external platforms work with Kaiser, and how to access telehealth mental health care. Updated 2026.',
    'life-transitions.html':
        'Best online therapy for life transitions. Expert-reviewed platforms with therapists in adjustment, grief, and major change. Real pricing and insurance. Updated 2026.',
    'magellan.html':
        'Does Magellan Health cover online therapy? See how Magellan behavioral health benefits work and which online platforms are in-network. Updated 2026.',
    'medicare.html':
        'Does Medicare cover online therapy? Yes — Part B covers telehealth mental health. Compare covered platforms, copay estimates, and how to access care. Updated 2026.',
    'mens-mental-health.html':
        'Best online therapy for men\'s mental health. Expert-reviewed platforms with therapists who understand masculine stress, identity, and stigma. Updated 2026.',
    'online-therapy-com-review.html':
        'Online-Therapy.com review 2026: structured CBT from $60/week with worksheets and live sessions. Honest pros, cons, and who it\'s best for. No sponsored rankings.',
    'panic.html':
        'Best online therapy for panic disorder. Expert-reviewed CBT platforms for managing and reducing panic attacks. Real pricing and insurance details. Updated 2026.',
    'phobias.html':
        'Best online therapy for phobias. Expert-reviewed platforms using CBT and exposure therapy for specific fears. Real pricing and insurance details. Updated 2026.',
    'privacy-policy.html':
        'Digital Therapy Solutions privacy policy. Plain English. We don\'t track you, sell your data, or use advertising pixels. Your privacy is taken seriously.',
    'relationship.html':
        'Best online therapy for relationship issues. Expert-reviewed platforms for dating, family, and friendship challenges. Individual therapy options. Updated 2026.',
    'social-anxiety.html':
        'Best online therapy for social anxiety. Expert-reviewed CBT platforms with exposure-based treatment options. Real pricing and insurance details. Updated 2026.',
    'tricare.html':
        'Does Tricare cover online therapy? Yes. Compare covered platforms, copay expectations, and how active duty, veterans, and military families can access care. Updated 2026.',
    'tufts.html':
        'Does Tufts Health Plan cover online therapy? Yes. Compare in-network platforms, expected copays, and how to access telehealth mental health benefits. Updated 2026.',
    'womens-mental-health.html':
        'Best online therapy for women\'s mental health. Expert-reviewed platforms with therapists in hormonal, relational, and identity-focused care. Updated 2026.',
}

OUTPUT_DIR = pathlib.Path('output')
fixed = 0
for filename, new_desc in FIXES.items():
    f = OUTPUT_DIR / filename
    if not f.exists():
        print(f"SKIP (not found): {filename}")
        continue
    n = len(new_desc)
    if n < 120 or n > 160:
        print(f"WARNING: {filename} desc is {n} chars — REVIEW: {new_desc}")
    content = f.read_text(encoding='utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    tag = soup.find('meta', {'name': 'description'})
    if tag:
        tag['content'] = new_desc
    else:
        # create it after charset
        charset = soup.find('meta', {'charset': True})
        new_tag = soup.new_tag('meta', attrs={'name': 'description', 'content': new_desc})
        if charset:
            charset.insert_after(new_tag)
        else:
            soup.head.insert(0, new_tag)
    f.write_text(str(soup), encoding='utf-8')
    fixed += 1
    print(f"FIXED [{n}]: {filename}")

print(f"\nDone. {fixed} files updated.")
