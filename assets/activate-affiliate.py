import sys
import re
import argparse
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

def activate(platform, url):
    output_dir = Path(__file__).parent.parent / 'output'
    target = output_dir / f'{platform}-review.html'
    if not target.exists():
        print(f'ERROR: {target} not found')
        sys.exit(1)
    html = target.read_text(encoding='utf-8')
    # Derive display name from slug
    name = platform.replace('-', ' ').title()
    # Replace all CTA buttons for this platform
    # Pattern: <a href="#" class="cta-button cta-button--pending" data-affiliate-status="pending" data-platform="SLUG">Coming Soon — Check Back</a>
    pattern = re.compile(
        r'<a\s+href="#"\s+class="cta-button cta-button--pending"\s+data-affiliate-status="pending"\s+data-platform="'
        + re.escape(platform) +
        r'">[^<]*</a>',
        re.IGNORECASE | re.DOTALL
    )
    replacement = f'<a href="{url}" class="cta-button" data-affiliate-status="active" data-platform="{platform}">Visit {name} &#x2192;</a>'
    new_html, count = pattern.subn(replacement, html)
    if count == 0:
        print(f'WARNING: No pending CTAs found for {platform} in {target.name}')
    target.write_text(new_html, encoding='utf-8')
    print(f'Activated {platform} -> {url} ({count} CTA(s) updated)')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Activate affiliate CTA for a platform')
    parser.add_argument('--platform', required=True, help='Platform slug (e.g. betterhelp)')
    parser.add_argument('--url', required=True, help='Affiliate URL')
    args = parser.parse_args()
    activate(args.platform, args.url)
