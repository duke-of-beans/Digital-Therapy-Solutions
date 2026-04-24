"""
prepare-condition-ctas.py
=========================
Audit and repair tool for condition/insurance page CTAs.

Ensures all non-review CTAs are affiliate-ready before running activate-affiliate.py:
  - Reports current CTA status across condition and insurance pages
  - Detects any bare href="#" CTAs not tagged with data-affiliate-status
  - Optionally adds data-affiliate-status="pending" to untagged CTAs (--fix flag)

Usage:
  python assets/prepare-condition-ctas.py           -- audit only (safe, no writes)
  python assets/prepare-condition-ctas.py --fix     -- add pending attribute to bare CTAs
  python assets/prepare-condition-ctas.py --fix --dry-run  -- preview --fix changes
"""

import sys
import re
import os
import argparse
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

OUTPUT_DIR = Path(__file__).parent.parent / 'output'

# Pages excluded from condition/insurance scan
EXCLUDED = {
    'index.html', 'about.html', 'reviews.html', 'conditions.html', 'insurance.html',
    'editorial-policy.html', 'affiliate-disclosure.html', 'privacy-policy.html',
    'crisis-resources.html', 'how-online-therapy-works.html', 'do-i-need-therapy.html',
    '404.html',
}

CTA_RE = re.compile(r'<a\b[^>]*cta-button[^>]*>[^<]*</a>', re.IGNORECASE | re.DOTALL)
BARE_RE = re.compile(
    r'<a\b(?=[^>]*href="#")(?=[^>]*cta-button)(?![^>]*data-affiliate-status)[^>]*>[^<]*</a>',
    re.IGNORECASE | re.DOTALL
)


def scan_pages():
    pages = sorted(
        p for p in OUTPUT_DIR.glob('*.html')
        if p.name not in EXCLUDED and 'review' not in p.name
    )

    status_counts = {'direct': 0, 'pending': 0, 'active': 0, 'bare': 0, 'other': 0}
    bare_files = []
    total_ctas = 0

    print(f"\n{'Page':<40} {'CTAs':>5}  {'direct':>6}  {'pending':>7}  {'active':>6}  {'bare':>5}  {'other':>5}")
    print('-' * 82)

    for page in pages:
        html = page.read_text(encoding='utf-8')
        ctas = CTA_RE.findall(html)
        total_ctas += len(ctas)
        row = {'direct': 0, 'pending': 0, 'active': 0, 'bare': 0, 'other': 0}

        for cta in ctas:
            if 'data-affiliate-status="direct"' in cta:
                row['direct'] += 1
            elif 'data-affiliate-status="pending"' in cta:
                row['pending'] += 1
            elif 'data-affiliate-status="active"' in cta:
                row['active'] += 1
            elif 'href="#"' in cta:
                row['bare'] += 1
            else:
                row['other'] += 1

        for k, v in row.items():
            status_counts[k] += v

        if row['bare'] > 0:
            bare_files.append(page.name)

        print(f"  {page.name:<38} {len(ctas):>5}  {row['direct']:>6}  {row['pending']:>7}  "
              f"{row['active']:>6}  {row['bare']:>5}  {row['other']:>5}")

    print('-' * 82)
    print(f"  {'TOTAL':<38} {total_ctas:>5}  {status_counts['direct']:>6}  "
          f"{status_counts['pending']:>7}  {status_counts['active']:>6}  "
          f"{status_counts['bare']:>5}  {status_counts['other']:>5}")
    print()

    return bare_files, status_counts


def fix_bare_ctas(dry_run=False):
    """Add data-affiliate-status='pending' to any bare href='#' CTA buttons."""
    pages = sorted(
        p for p in OUTPUT_DIR.glob('*.html')
        if p.name not in EXCLUDED and 'review' not in p.name
    )

    total_fixed = 0
    files_fixed = []

    for page in pages:
        html = page.read_text(encoding='utf-8')
        bare_ctas = BARE_RE.findall(html)
        if not bare_ctas:
            continue

        fixed_html = html
        for cta in bare_ctas:
            # Insert data-affiliate-status="pending" before the closing >
            # Find the position just before the > of the opening tag
            fixed_cta = re.sub(
                r'(<a\b[^>]*)(>)',
                r'\1 data-affiliate-status="pending"\2',
                cta,
                count=1,
                flags=re.IGNORECASE | re.DOTALL
            )
            fixed_html = fixed_html.replace(cta, fixed_cta, 1)

        count = len(bare_ctas)
        total_fixed += count
        files_fixed.append((page.name, count))

        print(f"  {'[DRY RUN] ' if dry_run else ''}Fixed {count} bare CTA(s) in {page.name}")
        for cta in bare_ctas:
            print(f"    BEFORE: {cta[:120]}")

        if not dry_run:
            page.write_text(fixed_html, encoding='utf-8')

    if total_fixed == 0:
        print("  ✅ No bare href='#' CTAs found — all condition/insurance pages are affiliate-ready.")
    else:
        print(f"\n  {'[DRY RUN] ' if dry_run else ''}Total: {total_fixed} CTA(s) across {len(files_fixed)} file(s)")
        if dry_run:
            print("  Re-run without --dry-run to apply changes.")

    return total_fixed


def main():
    parser = argparse.ArgumentParser(
        description='Audit and repair condition/insurance CTAs for affiliate activation'
    )
    parser.add_argument('--fix', action='store_true',
                        help='Add data-affiliate-status="pending" to bare href="#" CTAs')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview --fix changes without writing files')
    args = parser.parse_args()

    print('\n=== DTS Condition/Insurance CTA Status ===')
    bare_files, counts = scan_pages()

    if bare_files:
        print(f"⚠️  {counts['bare']} bare href='#' CTA(s) detected on {len(bare_files)} page(s):")
        for f in bare_files:
            print(f"    {f}")
        print("\nRun with --fix to add data-affiliate-status='pending' to these CTAs.")
        print("Run with --fix --dry-run to preview changes first.")
    else:
        print("✅ All condition/insurance CTAs have affiliate status attributes.")
        print(f"   direct={counts['direct']}  pending={counts['pending']}  "
              f"active={counts['active']}  other={counts['other']}")

    if args.fix:
        print('\n=== Applying Fixes ===')
        fix_bare_ctas(dry_run=args.dry_run)


if __name__ == '__main__':
    main()
