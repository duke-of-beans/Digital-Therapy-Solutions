import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

output_dir = Path(r'D:\Work\Digital-Therapy-Solutions\output')
checks = [
    ('nocd-review.html', ['nocd', 'data-platform="nocd"', 'cta-button--pending', 'BreadcrumbList', 'Review']),
    ('grow-therapy-review.html', ['grow-therapy', 'data-platform="grow-therapy"', 'cta-button--pending', 'BreadcrumbList', 'Review']),
    ('reviews.html', ['betterhelp-review.html', 'talkspace-review.html', 'nocd-review.html', 'grow-therapy-review.html', 'therapyden-review.html', 'Read Review']),
]

all_pass = True
for filename, required in checks:
    html = (output_dir / filename).read_text(encoding='utf-8')
    for term in required:
        if term not in html:
            print(f'FAIL [{filename}] missing: {term}')
            all_pass = False
        else:
            print(f'  OK [{filename}] {term}')

reviews = (output_dir / 'reviews.html').read_text(encoding='utf-8')
stubs = reviews.count('hub-card--stub')
live_ctas = reviews.count('hub-card__cta" href=')
print(f'\nreviews.html: {live_ctas} live CTAs, {stubs} stubs remaining')

pages = list(output_dir.glob('*-review.html'))
pending_count = sum(p.read_text(encoding='utf-8').count('cta-button--pending') for p in pages)
print(f'Total pending CTAs across {len(pages)} review pages: {pending_count}')
print(f'\nSpot-check: {"ALL PASS" if all_pass else "FAILURES FOUND"}')
