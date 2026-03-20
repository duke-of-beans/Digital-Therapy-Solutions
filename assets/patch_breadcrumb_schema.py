import sys, pathlib, json
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

DOMAIN = 'https://digitaltherapysolutions.com'

# Map: filename -> list of (name, url) breadcrumb items
# Home is always item 1. Hub is item 2 for detail pages. Page is last.
BREADCRUMBS = {
    # --- Homepage (1-item) ---
    'index.html': [
        ('Home', f'{DOMAIN}/'),
    ],
    # --- Hub pages (2-item) ---
    'conditions.html': [
        ('Home', f'{DOMAIN}/'),
        ('Conditions', f'{DOMAIN}/conditions'),
    ],
    'reviews.html': [
        ('Home', f'{DOMAIN}/'),
        ('Reviews', f'{DOMAIN}/reviews'),
    ],
    'insurance.html': [
        ('Home', f'{DOMAIN}/'),
        ('Insurance', f'{DOMAIN}/insurance'),
    ],
    # --- Supporting pages (2-item) ---
    'about.html': [
        ('Home', f'{DOMAIN}/'),
        ('About', f'{DOMAIN}/about'),
    ],
    'how-online-therapy-works.html': [
        ('Home', f'{DOMAIN}/'),
        ('How Online Therapy Works', f'{DOMAIN}/how-online-therapy-works'),
    ],
    'do-i-need-therapy.html': [
        ('Home', f'{DOMAIN}/'),
        ('Do I Need Therapy?', f'{DOMAIN}/do-i-need-therapy'),
    ],
    'crisis-resources.html': [
        ('Home', f'{DOMAIN}/'),
        ('Crisis Resources', f'{DOMAIN}/crisis-resources'),
    ],
    'editorial-policy.html': [
        ('Home', f'{DOMAIN}/'),
        ('Editorial Policy', f'{DOMAIN}/editorial-policy'),
    ],
    'affiliate-disclosure.html': [
        ('Home', f'{DOMAIN}/'),
        ('Affiliate Disclosure', f'{DOMAIN}/affiliate-disclosure'),
    ],
    'privacy-policy.html': [
        ('Home', f'{DOMAIN}/'),
        ('Privacy Policy', f'{DOMAIN}/privacy-policy'),
    ],
    # --- Condition pages (3-item) ---
    'anxiety.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Anxiety', f'{DOMAIN}/anxiety')],
    'depression.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Depression', f'{DOMAIN}/depression')],
    'adhd.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('ADHD', f'{DOMAIN}/adhd')],
    'couples.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Couples Therapy', f'{DOMAIN}/couples')],
    'ocd.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('OCD', f'{DOMAIN}/ocd')],
    'ptsd.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('PTSD', f'{DOMAIN}/ptsd')],
    'bipolar.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Bipolar Disorder', f'{DOMAIN}/bipolar')],
    'eating-disorders.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Eating Disorders', f'{DOMAIN}/eating-disorders')],
    'grief.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Grief & Loss', f'{DOMAIN}/grief')],
    'anger.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Anger Management', f'{DOMAIN}/anger')],
    'addiction.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Addiction', f'{DOMAIN}/addiction')],
    'stress.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Stress', f'{DOMAIN}/stress')],
    'burnout.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Burnout', f'{DOMAIN}/burnout')],
    'relationship.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Relationship Issues', f'{DOMAIN}/relationship')],
    'lgbtq.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('LGBTQ+ Therapy', f'{DOMAIN}/lgbtq')],
    'teen.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Teen Therapy', f'{DOMAIN}/teen')],
    'postpartum.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Postpartum Depression', f'{DOMAIN}/postpartum')],
    'insomnia.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Insomnia', f'{DOMAIN}/insomnia')],
    'chronic-pain.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Chronic Pain', f'{DOMAIN}/chronic-pain')],
    'social-anxiety.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Social Anxiety', f'{DOMAIN}/social-anxiety')],
    'phobias.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Phobias', f'{DOMAIN}/phobias')],
    'panic.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Panic Disorder', f'{DOMAIN}/panic')],
    'loneliness.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Loneliness', f'{DOMAIN}/loneliness')],
    'self-esteem.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Self-Esteem', f'{DOMAIN}/self-esteem')],
    'mens-mental-health.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ("Men's Mental Health", f'{DOMAIN}/mens-mental-health')],
    'womens-mental-health.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ("Women's Mental Health", f'{DOMAIN}/womens-mental-health')],
    'life-transitions.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Life Transitions', f'{DOMAIN}/life-transitions')],
    'autism.html': [('Home', f'{DOMAIN}/'), ('Conditions', f'{DOMAIN}/conditions'), ('Autism & Neurodivergence', f'{DOMAIN}/autism')],
    # --- Insurance pages (3-item) ---
    'aetna.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Aetna', f'{DOMAIN}/aetna')],
    'bcbs.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Blue Cross Blue Shield', f'{DOMAIN}/bcbs')],
    'cigna.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Cigna', f'{DOMAIN}/cigna')],
    'unitedhealthcare.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('UnitedHealthcare', f'{DOMAIN}/unitedhealthcare')],
    'medicaid.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Medicaid', f'{DOMAIN}/medicaid')],
    'affordable.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('ACA / Marketplace Plans', f'{DOMAIN}/affordable')],
    'humana.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Humana', f'{DOMAIN}/humana')],
    'kaiser.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Kaiser Permanente', f'{DOMAIN}/kaiser')],
    'anthem.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Anthem', f'{DOMAIN}/anthem')],
    'molina.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Molina Healthcare', f'{DOMAIN}/molina')],
    'oscar.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Oscar Health', f'{DOMAIN}/oscar')],
    'ambetter.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Ambetter', f'{DOMAIN}/ambetter')],
    'wellcare.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('WellCare', f'{DOMAIN}/wellcare')],
    'tricare.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Tricare', f'{DOMAIN}/tricare')],
    'chip.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('CHIP', f'{DOMAIN}/chip')],
    'medicare.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Medicare', f'{DOMAIN}/medicare')],
    'beacon.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Beacon Health Options', f'{DOMAIN}/beacon')],
    'magellan.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Magellan Health', f'{DOMAIN}/magellan')],
    'centene.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Centene', f'{DOMAIN}/centene')],
    'highmark.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Highmark', f'{DOMAIN}/highmark')],
    'harvard-pilgrim.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Harvard Pilgrim', f'{DOMAIN}/harvard-pilgrim')],
    'tufts.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Tufts Health Plan', f'{DOMAIN}/tufts')],
    'community-health.html': [('Home', f'{DOMAIN}/'), ('Insurance', f'{DOMAIN}/insurance'), ('Community Health Plans', f'{DOMAIN}/community-health')],
    # --- Review pages (3-item) ---
    'betterhelp-review.html': [('Home', f'{DOMAIN}/'), ('Reviews', f'{DOMAIN}/reviews'), ('BetterHelp Review', f'{DOMAIN}/betterhelp-review')],
    'talkspace-review.html': [('Home', f'{DOMAIN}/'), ('Reviews', f'{DOMAIN}/reviews'), ('Talkspace Review', f'{DOMAIN}/talkspace-review')],
    'online-therapy-com-review.html': [('Home', f'{DOMAIN}/'), ('Reviews', f'{DOMAIN}/reviews'), ('Online-Therapy.com Review', f'{DOMAIN}/online-therapy-com-review')],
}

def make_breadcrumb_schema(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                "item": url
            }
            for i, (name, url) in enumerate(items)
        ]
    }

OUTPUT_DIR = pathlib.Path('output')
added = 0
skipped = 0
missing_map = 0

for f in sorted(OUTPUT_DIR.glob('*.html')):
    if f.name not in BREADCRUMBS:
        print(f"NO MAP ENTRY: {f.name}")
        missing_map += 1
        continue

    content = f.read_text(encoding='utf-8')
    soup = BeautifulSoup(content, 'html.parser')

    # Check if BreadcrumbList already present
    scripts = soup.find_all('script', {'type': 'application/ld+json'})
    for s in scripts:
        if s.string and 'BreadcrumbList' in s.string:
            skipped += 1
            print(f"ALREADY PRESENT: {f.name}")
            break
    else:
        schema = make_breadcrumb_schema(BREADCRUMBS[f.name])
        script_tag = soup.new_tag('script', attrs={'type': 'application/ld+json'})
        script_tag.string = json.dumps(schema, ensure_ascii=False, indent=2)
        soup.head.append(script_tag)
        f.write_text(str(soup), encoding='utf-8')
        added += 1
        print(f"ADDED: {f.name}")

print(f"\nDone. Added: {added}, Already present: {skipped}, No map: {missing_map}")
