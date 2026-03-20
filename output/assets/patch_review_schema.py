import sys, pathlib, json
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

REVIEWS = {
    'betterhelp-review.html': {
        "@context": "https://schema.org",
        "@type": "Review",
        "itemReviewed": {
            "@type": "SoftwareApplication",
            "name": "BetterHelp",
            "applicationCategory": "Online Therapy Platform",
            "url": "https://www.betterhelp.com"
        },
        "reviewRating": {
            "@type": "Rating",
            "ratingValue": "4.5",
            "bestRating": "5"
        },
        "name": "BetterHelp Review 2026 — Honest Pros, Cons & Pricing",
        "author": {"@type": "Organization", "name": "Digital Therapy Solutions"},
        "publisher": {
            "@type": "Organization",
            "name": "Digital Therapy Solutions",
            "url": "https://digitaltherapysolutions.com"
        },
        "datePublished": "2026-01-01",
        "reviewBody": "BetterHelp is the largest online therapy platform with 30,000+ therapists. Strong for most people, best for those paying out of pocket without insurance needs."
    },
    'talkspace-review.html': {
        "@context": "https://schema.org",
        "@type": "Review",
        "itemReviewed": {
            "@type": "SoftwareApplication",
            "name": "Talkspace",
            "applicationCategory": "Online Therapy Platform",
            "url": "https://www.talkspace.com"
        },
        "reviewRating": {
            "@type": "Rating",
            "ratingValue": "4.3",
            "bestRating": "5"
        },
        "name": "Talkspace Review 2026 — Honest Pros, Cons & Pricing",
        "author": {"@type": "Organization", "name": "Digital Therapy Solutions"},
        "publisher": {
            "@type": "Organization",
            "name": "Digital Therapy Solutions",
            "url": "https://digitaltherapysolutions.com"
        },
        "datePublished": "2026-01-01",
        "reviewBody": "Talkspace is the best choice for insured clients — in-network with Aetna, Cigna, and others. Messaging-forward format suits people who prefer writing over video."
    },
    'online-therapy-com-review.html': {
        "@context": "https://schema.org",
        "@type": "Review",
        "itemReviewed": {
            "@type": "SoftwareApplication",
            "name": "Online-Therapy.com",
            "applicationCategory": "Online Therapy Platform",
            "url": "https://www.online-therapy.com"
        },
        "reviewRating": {
            "@type": "Rating",
            "ratingValue": "4.1",
            "bestRating": "5"
        },
        "name": "Online-Therapy.com Review 2026 — Honest Pros, Cons & Pricing",
        "author": {"@type": "Organization", "name": "Digital Therapy Solutions"},
        "publisher": {
            "@type": "Organization",
            "name": "Digital Therapy Solutions",
            "url": "https://digitaltherapysolutions.com"
        },
        "datePublished": "2026-01-01",
        "reviewBody": "Online-Therapy.com is built around structured CBT. Best for anxiety and depression where a clear program beats open-ended talk therapy. No insurance accepted."
    },
}

OUTPUT_DIR = pathlib.Path('output')
added = 0
skipped = 0

for filename, schema in REVIEWS.items():
    f = OUTPUT_DIR / filename
    if not f.exists():
        print(f"NOT FOUND: {filename}")
        continue
    content = f.read_text(encoding='utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    # Check existing Review schema
    for s in soup.find_all('script', {'type': 'application/ld+json'}):
        if s.string and '"Review"' in s.string:
            skipped += 1
            print(f"ALREADY PRESENT: {filename}")
            break
    else:
        script_tag = soup.new_tag('script', attrs={'type': 'application/ld+json'})
        script_tag.string = json.dumps(schema, ensure_ascii=False, indent=2)
        soup.head.append(script_tag)
        f.write_text(str(soup), encoding='utf-8')
        added += 1
        print(f"ADDED: {filename}")

print(f"\nDone. Added: {added}, Already present: {skipped}")
