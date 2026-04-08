"""
patch-cta-direct.py
===================
Patches ALL condition and insurance pages in output/ to:
  1. Replace bare href="#" CTAs with direct platform URLs + data-platform attribute
  2. Convert <button class="button button--primary"> CTAs to proper <a> tags
  3. Add data-affiliate-status="direct" to all CTA anchors
  4. Fix broken --clr-primary CSS variable -> --accent-primary across all HTML files
  5. Fix "See full review" meta links to point to review pages

Run: python assets/patch-cta-direct.py
     python assets/patch-cta-direct.py --dry-run   (preview only)
     python assets/patch-cta-direct.py --fix-css-only
"""

import sys
import re
import json
import argparse
from pathlib import Path
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')

# ── Load registry ─────────────────────────────────────────────────────────────

REGISTRY_PATH = Path(__file__).parent / 'platform-registry.json'
registry = json.loads(REGISTRY_PATH.read_text(encoding='utf-8'))
PLATFORMS = registry['platforms']
NAME_TO_SLUG = registry['name_to_slug']

OUTPUT_DIR = Path(__file__).parent.parent / 'output'

# Pages to SKIP (review pages handled by activate-affiliate.py)
REVIEW_SUFFIX = '-review.html'

# Pages to process: condition + insurance pages only
SKIP_PAGES = {
    'index.html', 'about.html', 'reviews.html', 'conditions.html',
    'insurance.html', 'editorial-policy.html', 'affiliate-disclosure.html',
    'privacy-policy.html', 'crisis-resources.html', 'how-online-therapy-works.html',
    'do-i-need-therapy.html', '404.html', 'sitemap.xml', 'robots.txt',
}


def is_review_page(filename):
    return filename.endswith(REVIEW_SUFFIX)


def is_target_page(filename):
    if filename in SKIP_PAGES:
        return False
    if is_review_page(filename):
        return False
    return filename.endswith('.html')


# ── Name extraction from HTML ─────────────────────────────────────────────────

def extract_platform_names_from_html(html):
    """Extract platform names from .platform-card__name h3 elements."""
    pattern = re.compile(
        r'<h3[^>]*class="platform-card__name"[^>]*>(.*?)</h3>',
        re.IGNORECASE | re.DOTALL
    )
    names = []
    for m in pattern.finditer(html):
        name = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        names.append(name)
    return names


def resolve_slug(name):
    """Map a display name to a registry slug."""
    # Direct match
    if name in NAME_TO_SLUG:
        return NAME_TO_SLUG[name]
    # Case-insensitive fallback
    name_lower = name.lower()
    for k, v in NAME_TO_SLUG.items():
        if k.lower() == name_lower:
            return v
    return None


# ── CTA Patching ──────────────────────────────────────────────────────────────

def patch_cta_section(cta_block, slug, platform_info):
    """
    Given a .platform-card__cta block HTML string and a platform slug,
    replace any bare href="#" <a> or <button> CTA with a proper direct link.
    Returns patched block.
    """
    direct_url = platform_info['direct_url']

    # Pattern 1: <a class="cta-button" href="#">TEXT</a>
    def replace_anchor(m):
        full = m.group(0)
        # Already has data-affiliate-status set to something real -> skip
        if 'data-affiliate-status="active"' in full:
            return full
        # Extract text content
        text_match = re.search(r'>(.*?)</a>', full, re.DOTALL)
        text = text_match.group(1).strip() if text_match else 'Visit Platform'
        return (
            f'<a class="cta-button" href="{direct_url}" '
            f'data-platform="{slug}" data-affiliate-status="direct" '
            f'target="_blank" rel="noopener">{text}</a>'
        )

    patched = re.sub(
        r'<a\s+class="cta-button"[^>]*href="#"[^>]*>.*?</a>',
        replace_anchor,
        cta_block,
        flags=re.DOTALL | re.IGNORECASE
    )

    # Also catch reversed attribute order: href="#" class="cta-button"
    patched = re.sub(
        r'<a\s+href="#"\s+class="cta-button"[^>]*>.*?</a>',
        replace_anchor,
        patched,
        flags=re.DOTALL | re.IGNORECASE
    )

    # Pattern 2: <button class="button button--primary">TEXT</button>
    def replace_button(m):
        text_match = re.search(r'>(.*?)</button>', m.group(0), re.DOTALL)
        text = text_match.group(1).strip() if text_match else 'Visit Platform'
        return (
            f'<a class="cta-button" href="{direct_url}" '
            f'data-platform="{slug}" data-affiliate-status="direct" '
            f'target="_blank" rel="noopener">{text}</a>'
        )

    patched = re.sub(
        r'<button[^>]*class="button button--primary"[^>]*>.*?</button>',
        replace_button,
        patched,
        flags=re.DOTALL | re.IGNORECASE
    )

    return patched


def patch_meta_review_link(meta_block, slug, platform_info):
    """Fix 'See full review ->' link in .platform-card__meta to point to review page."""
    review_page = platform_info.get('review_page', '')
    if not review_page:
        return meta_block

    # Replace href="#" on meta links
    def replace_meta(m):
        full = m.group(0)
        if 'href="#"' in full or "href='#'" in full:
            return re.sub(r'href=["\']#["\']', f'href="{review_page}"', full)
        return full

    return re.sub(
        r'<a[^>]*class="meta-link"[^>]*>.*?</a>',
        replace_meta,
        meta_block,
        flags=re.DOTALL | re.IGNORECASE
    )


def patch_html_file(html_path, dry_run=False):
    """
    Main patch function for a single HTML file.
    Returns (patched_html, change_summary).
    """
    html = html_path.read_text(encoding='utf-8')
    original = html
    changes = []

    # ── Step 1: Extract platform names from this page ──────────────────────
    platform_names = extract_platform_names_from_html(html)
    if not platform_names:
        return html, ['No platform cards found — skipped']

    # ── Step 2: Split HTML into platform-card sections ─────────────────────
    # We process each card section individually so we know which platform it is
    # Split on <article class="platform-card
    card_pattern = re.compile(
        r'(<article[^>]*class="[^"]*platform-card[^"]*"[^>]*>)(.*?)(</article>)',
        re.DOTALL | re.IGNORECASE
    )

    card_index = [0]  # mutable for closure

    def patch_card(m):
        open_tag = m.group(1)
        body = m.group(2)
        close_tag = m.group(3)
        idx = card_index[0]
        card_index[0] += 1

        if idx >= len(platform_names):
            return m.group(0)  # More cards than names extracted — skip

        name = platform_names[idx]
        slug = resolve_slug(name)

        if not slug:
            changes.append(f'  WARN: Could not resolve slug for "{name}" (card {idx})')
            return m.group(0)

        platform_info = PLATFORMS.get(slug)
        if not platform_info:
            changes.append(f'  WARN: Slug "{slug}" not in registry (card {idx})')
            return m.group(0)

        # Patch .platform-card__cta section within this card
        cta_pattern = re.compile(
            r'(<div[^>]*class="platform-card__cta"[^>]*>)(.*?)(</div>)',
            re.DOTALL | re.IGNORECASE
        )
        patched_body = body
        cta_match = cta_pattern.search(body)
        if cta_match:
            original_cta = cta_match.group(0)
            patched_cta_inner = patch_cta_section(cta_match.group(2), slug, platform_info)
            patched_cta = cta_match.group(1) + patched_cta_inner + cta_match.group(3)
            if patched_cta != original_cta:
                patched_body = patched_body.replace(original_cta, patched_cta, 1)
                changes.append(f'  PATCHED CTA: {name} ({slug}) -> {platform_info["direct_url"]}')

        # Patch .platform-card__meta review link
        meta_pattern = re.compile(
            r'(<div[^>]*class="platform-card__meta"[^>]*>)(.*?)(</div>)',
            re.DOTALL | re.IGNORECASE
        )
        meta_match = meta_pattern.search(patched_body)
        if meta_match:
            original_meta = meta_match.group(0)
            patched_meta_inner = patch_meta_review_link(meta_match.group(2), slug, platform_info)
            patched_meta = meta_match.group(1) + patched_meta_inner + meta_match.group(3)
            if patched_meta != original_meta:
                patched_body = patched_body.replace(original_meta, patched_meta, 1)
                changes.append(f'  FIXED meta link: {name} -> {platform_info["review_page"]}')

        return open_tag + patched_body + close_tag

    patched_html = card_pattern.sub(patch_card, html)

    # ── Step 3: Fix --clr-primary -> --accent-primary ──────────────────────
    clr_count = patched_html.count('var(--clr-primary)')
    if clr_count > 0:
        patched_html = patched_html.replace('var(--clr-primary)', 'var(--accent-primary)')
        changes.append(f'  FIXED CSS: --clr-primary -> --accent-primary ({clr_count} occurrences)')

    if patched_html == original:
        changes.append('  No changes needed')

    if not dry_run and patched_html != original:
        html_path.write_text(patched_html, encoding='utf-8')

    return patched_html, changes


# ── CSS-only fix (all 97 pages) ───────────────────────────────────────────────

def fix_css_variable_all_pages(dry_run=False):
    """Fix --clr-primary across ALL output HTML files."""
    total = 0
    for html_path in sorted(OUTPUT_DIR.glob('*.html')):
        html = html_path.read_text(encoding='utf-8')
        count = html.count('var(--clr-primary)')
        if count > 0:
            if not dry_run:
                html_path.write_text(
                    html.replace('var(--clr-primary)', 'var(--accent-primary)'),
                    encoding='utf-8'
                )
            print(f'  {html_path.name}: fixed {count} occurrence(s)')
            total += count
    print(f'\nTotal --clr-primary fixes: {total}')


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Patch condition/insurance page CTAs to use direct platform links')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without writing')
    parser.add_argument('--fix-css-only', action='store_true', help='Only fix --clr-primary across all pages')
    parser.add_argument('--file', help='Process a single file only (filename, e.g. anxiety.html)')
    args = parser.parse_args()

    if args.fix_css_only:
        print('Fixing --clr-primary -> --accent-primary across all pages...')
        fix_css_variable_all_pages(dry_run=args.dry_run)
        return

    if args.dry_run:
        print('DRY RUN — no files will be written\n')

    if args.file:
        targets = [OUTPUT_DIR / args.file]
    else:
        targets = sorted(
            f for f in OUTPUT_DIR.glob('*.html')
            if is_target_page(f.name)
        )

    print(f'Processing {len(targets)} target page(s)...\n')
    patched_count = 0

    for html_path in targets:
        _, changes = patch_html_file(html_path, dry_run=args.dry_run)
        has_changes = any('PATCHED' in c or 'FIXED' in c for c in changes)
        status = 'CHANGED' if has_changes else 'clean'
        print(f'[{status}] {html_path.name}')
        for c in changes:
            print(c)
        if has_changes:
            patched_count += 1

    print(f'\n{"DRY RUN " if args.dry_run else ""}Done. {patched_count}/{len(targets)} pages modified.')
    if args.dry_run:
        print('Re-run without --dry-run to apply changes.')


if __name__ == '__main__':
    main()
