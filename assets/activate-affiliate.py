"""
activate-affiliate.py
=====================
Activates affiliate CTAs for a platform across ALL output pages
(review pages, condition pages, insurance pages).

Usage:
  python assets/activate-affiliate.py --platform betterhelp --url https://www.betterhelp.com/go/?m=...
  python assets/activate-affiliate.py --list    (show all platforms and current status)
  python assets/activate-affiliate.py --status  (show which platforms are active vs direct)

Matches:
  data-affiliate-status="direct"   (set by patch-cta-direct.py — direct/no-affiliate link)
  data-affiliate-status="pending"  (legacy — old review page pattern)

Replaces with:
  data-affiliate-status="active"   + affiliate URL
"""

import sys
import re
import json
import argparse
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

REGISTRY_PATH = Path(__file__).parent / 'platform-registry.json'
OUTPUT_DIR = Path(__file__).parent.parent / 'output'


def load_registry():
    return json.loads(REGISTRY_PATH.read_text(encoding='utf-8'))


def activate(platform, url, dry_run=False):
    registry = load_registry()
    platforms = registry['platforms']

    if platform not in platforms:
        print(f'ERROR: "{platform}" not found in platform-registry.json')
        print('Run --list to see available platforms.')
        sys.exit(1)

    platform_info = platforms[platform]
    display_name = platform_info['name']

    # Patterns to match (both direct and legacy pending)
    patterns = [
        # data-affiliate-status="direct" pattern (new)
        re.compile(
            r'<a([^>]*)data-platform="' + re.escape(platform) + r'"([^>]*)data-affiliate-status="direct"([^>]*)>(.*?)</a>',
            re.IGNORECASE | re.DOTALL
        ),
        # reversed attribute order
        re.compile(
            r'<a([^>]*)data-affiliate-status="direct"([^>]*)data-platform="' + re.escape(platform) + r'"([^>]*)>(.*?)</a>',
            re.IGNORECASE | re.DOTALL
        ),
        # Legacy pending pattern — order-independent attribute matching
        re.compile(
            r'<a\b(?=[^>]*href="#")(?=[^>]*class="cta-button cta-button--pending")(?=[^>]*data-affiliate-status="pending")(?=[^>]*data-platform="'
            + re.escape(platform) +
            r'")[^>]*>[^<]*</a>',
            re.IGNORECASE | re.DOTALL
        ),
    ]

    total_updated = 0
    files_updated = []

    for html_path in sorted(OUTPUT_DIR.glob('*.html')):
        html = html_path.read_text(encoding='utf-8')
        original = html
        file_count = 0

        # Pattern 1 & 2: direct status (preserves CTA text)
        def replace_direct(m):
            # Reconstruct with affiliate URL, preserve existing text and class
            full = m.group(0)
            # Extract inner text
            text_match = re.search(r'>([^<]*)</a>', full)
            text = text_match.group(1).strip() if text_match else f'Visit {display_name}'
            return (
                f'<a class="cta-button" href="{url}" '
                f'data-platform="{platform}" data-affiliate-status="active" '
                f'target="_blank" rel="noopener sponsored">{text}</a>'
            )

        for pat in patterns[:2]:
            new_html, n = pat.subn(replace_direct, html)
            if n > 0:
                html = new_html
                file_count += n

        # Pattern 3: legacy pending (generates fresh text)
        legacy_replacement = (
            f'<a href="{url}" class="cta-button" '
            f'data-affiliate-status="active" data-platform="{platform}" '
            f'target="_blank" rel="noopener sponsored">Visit {display_name} &#x2192;</a>'
        )
        new_html, n = patterns[2].subn(legacy_replacement, html)
        if n > 0:
            html = new_html
            file_count += n

        if file_count > 0:
            total_updated += file_count
            files_updated.append((html_path.name, file_count))
            if not dry_run:
                html_path.write_text(html, encoding='utf-8')

    # Update registry with affiliate URL
    if not dry_run and total_updated > 0:
        registry['platforms'][platform]['affiliate_url'] = url
        REGISTRY_PATH.write_text(
            json.dumps(registry, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )
        print(f'Registry updated: {platform} affiliate_url set.')

    print(f'\nActivated: {display_name} -> {url}')
    print(f'CTAs updated: {total_updated} across {len(files_updated)} file(s)')
    for fname, count in files_updated:
        print(f'  {fname}: {count} CTA(s)')

    if dry_run:
        print('\nDRY RUN — no files written. Re-run without --dry-run to apply.')

    if total_updated == 0:
        print(f'\nWARNING: No CTAs found for "{platform}". Has patch-cta-direct.py been run?')


def list_platforms():
    registry = load_registry()
    platforms = registry['platforms']
    print(f'\n{"Platform":<30} {"Slug":<25} {"Affiliate?":<12} {"Status":<10} Network')
    print('-' * 100)
    for slug, info in sorted(platforms.items()):
        name = info['name']
        has_prog = 'Yes' if info['has_affiliate_program'] else 'No'
        status = 'ACTIVE' if info['affiliate_url'] else 'direct'
        network = info['affiliate_network'] or 'N/A'
        print(f'{name:<30} {slug:<25} {has_prog:<12} {status:<10} {network}')
    print()


def show_status():
    """Scan output pages and report CTA status per platform."""
    registry = load_registry()
    platforms = registry['platforms']

    counts = {slug: {'direct': 0, 'active': 0, 'files_direct': [], 'files_active': []} for slug in platforms}

    for html_path in sorted(OUTPUT_DIR.glob('*.html')):
        html = html_path.read_text(encoding='utf-8')
        for slug in platforms:
            direct_count = len(re.findall(
                r'data-platform="' + re.escape(slug) + r'"[^>]*data-affiliate-status="direct"',
                html, re.IGNORECASE
            ))
            active_count = len(re.findall(
                r'data-platform="' + re.escape(slug) + r'"[^>]*data-affiliate-status="active"',
                html, re.IGNORECASE
            ))
            if direct_count:
                counts[slug]['direct'] += direct_count
                counts[slug]['files_direct'].append(html_path.name)
            if active_count:
                counts[slug]['active'] += active_count
                counts[slug]['files_active'].append(html_path.name)

    print(f'\n{"Platform":<30} {"Direct CTAs":<14} {"Active CTAs":<14} Status')
    print('-' * 75)
    for slug, data in sorted(counts.items()):
        if data['direct'] == 0 and data['active'] == 0:
            continue
        name = platforms[slug]['name']
        status = 'LIVE' if data['active'] > 0 else 'pending'
        print(f'{name:<30} {data["direct"]:<14} {data["active"]:<14} {status}')
    print()


def main():
    parser = argparse.ArgumentParser(description='Activate affiliate CTAs across all DTS pages')
    parser.add_argument('--platform', help='Platform slug (e.g. betterhelp)')
    parser.add_argument('--url', help='Your affiliate URL for this platform')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    parser.add_argument('--list', action='store_true', help='List all platforms and affiliate status')
    parser.add_argument('--status', action='store_true', help='Show CTA status across all pages')
    args = parser.parse_args()

    if args.list:
        list_platforms()
        return

    if args.status:
        show_status()
        return

    if not args.platform or not args.url:
        parser.error('--platform and --url are required (or use --list / --status)')

    activate(args.platform, args.url, dry_run=args.dry_run)


if __name__ == '__main__':
    main()
