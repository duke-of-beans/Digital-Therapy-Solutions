import sys, pathlib, json
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

# Condition pages: (display_name, filename)
CONDITIONS = [
    ('Anxiety', 'anxiety.html'),
    ('Depression', 'depression.html'),
    ('ADHD', 'adhd.html'),
    ('Couples Therapy', 'couples.html'),
    ('OCD', 'ocd.html'),
    ('PTSD', 'ptsd.html'),
    ('Bipolar Disorder', 'bipolar.html'),
    ('Eating Disorders', 'eating-disorders.html'),
    ('Grief and Loss', 'grief.html'),
    ('Anger Management', 'anger.html'),
    ('Addiction', 'addiction.html'),
    ('Stress', 'stress.html'),
    ('Burnout', 'burnout.html'),
    ('Relationship Issues', 'relationship.html'),
    ('LGBTQ+ Issues', 'lgbtq.html'),
    ('Teen Mental Health', 'teen.html'),
    ('Postpartum Depression', 'postpartum.html'),
    ('Insomnia', 'insomnia.html'),
    ('Chronic Pain', 'chronic-pain.html'),
    ('Social Anxiety', 'social-anxiety.html'),
    ('Phobias', 'phobias.html'),
    ('Panic Disorder', 'panic.html'),
    ('Loneliness', 'loneliness.html'),
    ('Low Self-Esteem', 'self-esteem.html'),
    ("Men's Mental Health", 'mens-mental-health.html'),
    ("Women's Mental Health", 'womens-mental-health.html'),
    ('Life Transitions', 'life-transitions.html'),
    ('Autism and Neurodivergence', 'autism.html'),
]

# Insurance pages: (display_name, filename)
INSURANCES = [
    ('Aetna', 'aetna.html'),
    ('Blue Cross Blue Shield', 'bcbs.html'),
    ('Cigna', 'cigna.html'),
    ('UnitedHealthcare', 'unitedhealthcare.html'),
    ('Medicaid', 'medicaid.html'),
    ('ACA Marketplace plans', 'affordable.html'),
    ('Humana', 'humana.html'),
    ('Kaiser Permanente', 'kaiser.html'),
    ('Anthem', 'anthem.html'),
    ('Molina Healthcare', 'molina.html'),
    ('Oscar Health', 'oscar.html'),
    ('Ambetter', 'ambetter.html'),
    ('WellCare', 'wellcare.html'),
    ('Tricare', 'tricare.html'),
    ('CHIP', 'chip.html'),
    ('Medicare', 'medicare.html'),
    ('Beacon Health Options', 'beacon.html'),
    ('Magellan Health', 'magellan.html'),
    ('Centene', 'centene.html'),
    ('Highmark', 'highmark.html'),
    ('Harvard Pilgrim', 'harvard-pilgrim.html'),
    ('Tufts Health Plan', 'tufts.html'),
    ('Community Health Plans', 'community-health.html'),
]

def condition_faq(name):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f"Is online therapy effective for {name}?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"Yes — multiple studies support online therapy for {name}, with outcomes comparable to in-person treatment for most people."
                }
            },
            {
                "@type": "Question",
                "name": f"How much does online therapy for {name} cost?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Costs range from $45–100/week depending on the platform. With insurance, copays can bring this to $10–50/session."
                }
            },
            {
                "@type": "Question",
                "name": f"Which platform is best for {name}?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"It depends on your needs and budget. We review 34+ platforms and recommend the top 3 for {name} on this page."
                }
            }
        ]
    }

def insurance_faq(name):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f"Does {name} cover online therapy?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"Coverage depends on your specific plan. Many {name} plans include telehealth mental health benefits — check with your insurer or verify at signup."
                }
            },
            {
                "@type": "Question",
                "name": f"Which online therapy platforms accept {name}?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"Several platforms accept {name}, including Talkspace and others. The best options are listed on this page."
                }
            },
            {
                "@type": "Question",
                "name": f"How much will I pay for online therapy with {name}?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "With in-network coverage, copays typically range from $10–50/session depending on your deductible and plan type."
                }
            }
        ]
    }

OUTPUT_DIR = pathlib.Path('output')
added = 0
skipped = 0

def inject_faq(filename, schema):
    global added, skipped
    f = OUTPUT_DIR / filename
    if not f.exists():
        print(f"NOT FOUND: {filename}")
        return
    content = f.read_text(encoding='utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    # Check if FAQPage already present
    for s in soup.find_all('script', {'type': 'application/ld+json'}):
        if s.string and 'FAQPage' in s.string:
            skipped += 1
            print(f"ALREADY PRESENT: {filename}")
            return
    script_tag = soup.new_tag('script', attrs={'type': 'application/ld+json'})
    script_tag.string = json.dumps(schema, ensure_ascii=False, indent=2)
    soup.head.append(script_tag)
    f.write_text(str(soup), encoding='utf-8')
    added += 1
    print(f"ADDED: {filename}")

for name, fn in CONDITIONS:
    inject_faq(fn, condition_faq(name))

for name, fn in INSURANCES:
    inject_faq(fn, insurance_faq(name))

print(f"\nDone. Added: {added}, Already present: {skipped}")
