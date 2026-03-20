import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

output_dir = Path(r'D:\Work\Digital-Therapy-Solutions\output')

pages = [
    ('betterhelp-review.html', 'betterhelp'),
    ('talkspace-review.html', 'talkspace'),
    ('online-therapy-com-review.html', 'online-therapy-com'),
]

for filename, slug in pages:
    p = output_dir / filename
    html = p.read_text(encoding='utf-8')
    # Find CTA buttons that don't yet have data-affiliate-status
    # Pattern: <a class="cta-button" href="#">...
    # We need to add data-platform, data-affiliate-status, cta-button--pending
    count = 0
    def replace_cta(m):
        global count
        count += 1
        return (f'<a href="#" class="cta-button cta-button--pending" '
                f'data-affiliate-status="pending" data-platform="{slug}">'
                f'Coming Soon — Check Back</a>')
    # Match existing CTAs that don't yet have pending markup
    new_html = re.sub(
        r'<a\s+class="cta-button"\s+href="#">[^<]*</a>',
        replace_cta,
        html
    )
    p.write_text(new_html, encoding='utf-8')
    print(f'Retrofitted {filename}: {count} CTA(s)')
