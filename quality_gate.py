import os, re
import sys
sys.stdout.reconfigure(encoding='utf-8')

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

html_files = sorted([f for f in os.listdir(output_dir) if f.endswith('.html')])

failures = []
warnings = []

def check(fname, content):
    # 1. Favicon present
    if 'favicon.png' not in content:
        failures.append(f'[{fname}] MISSING: favicon')
    # 2. Apple touch icon
    if 'apple-touch-icon' not in content:
        failures.append(f'[{fname}] MISSING: apple-touch-icon')
    # 3. Logo icon in nav
    if 'logo-icon.webp' not in content:
        failures.append(f'[{fname}] MISSING: logo-icon.webp in nav')
    # 4. Crisis footer
    if '988' not in content:
        failures.append(f'[{fname}] MISSING: 988 crisis line in footer')
    if 'crisis-alert' not in content and 'crisis_alert' not in content:
        failures.append(f'[{fname}] MISSING: crisis-alert class')
    # 5. Styles.css linked
    if 'styles.css' not in content:
        failures.append(f'[{fname}] MISSING: styles.css link')
    # 6. Google Fonts
    if 'Fraunces' not in content:
        failures.append(f'[{fname}] MISSING: Fraunces font')
    # 7. Reveal classes
    if 'class="reveal"' not in content and "class='reveal'" not in content:
        warnings.append(f'[{fname}] WARNING: no .reveal sections')
    # 8. viewport meta
    if 'viewport' not in content:
        failures.append(f'[{fname}] MISSING: viewport meta')
    # 9. No hard CTAs on educational pages
    if fname in ['do-i-need-therapy.html', 'how-online-therapy-works.html']:
        # Should not have cta-button class (hard CTA)
        if 'class="cta-button"' in content:
            failures.append(f'[{fname}] FAIL: hard CTA button found on educational page')
    # 10. Trust badge
    if '34+' not in content and '34 +' not in content:
        warnings.append(f'[{fname}] WARNING: trust badge "34+" not found')
    # 11. Footer crisis line has "In crisis?"
    if 'In crisis?' not in content:
        failures.append(f'[{fname}] MISSING: "In crisis?" in footer')
    # 12. Index.html specific: should have condition tiles and insurance tiles
    if fname == 'index.html':
        if 'anxiety.html' not in content:
            failures.append(f'[{fname}] MISSING: anxiety.html link')
        if 'depression.html' not in content:
            failures.append(f'[{fname}] MISSING: depression.html link')
        if 'adhd.html' not in content:
            failures.append(f'[{fname}] MISSING: adhd.html link')
        if 'couples.html' not in content:
            failures.append(f'[{fname}] MISSING: couples.html link')
        if 'aetna.html' not in content:
            failures.append(f'[{fname}] MISSING: aetna.html link')
        if 'bcbs.html' not in content:
            failures.append(f'[{fname}] MISSING: bcbs.html link')
        if 'medicaid.html' not in content:
            failures.append(f'[{fname}] MISSING: medicaid.html link')
        if 'betterhelp-review.html' not in content:
            failures.append(f'[{fname}] MISSING: betterhelp-review.html link')
        if 'talkspace-review.html' not in content:
            failures.append(f'[{fname}] MISSING: talkspace-review.html link')
        if 'online-therapy-com-review.html' not in content:
            failures.append(f'[{fname}] MISSING: online-therapy-com-review.html link')
    # 13. Crisis resources page: 6+ resources
    if fname == 'crisis-resources.html':
        resource_count = content.count('tel:')
        if resource_count < 4:
            failures.append(f'[{fname}] FAIL: only {resource_count} phone links (need 4+)')
        if '988' not in content:
            failures.append(f'[{fname}] MISSING: 988')
        if '741741' not in content:
            failures.append(f'[{fname}] MISSING: Crisis Text Line 741741')
        if 'Trevor' not in content:
            failures.append(f'[{fname}] MISSING: Trevor Project')
        if 'Veterans' not in content and 'veteran' not in content.lower():
            failures.append(f'[{fname}] MISSING: Veterans Crisis Line')
        if 'SAMHSA' not in content:
            failures.append(f'[{fname}] MISSING: SAMHSA')
    # 14. About page: methodology content
    if fname == 'about.html':
        if 'methodology' not in content.lower() and 'research' not in content.lower():
            failures.append(f'[{fname}] MISSING: methodology content')
    # 15. Affiliate disclosure: FTC
    if fname == 'affiliate-disclosure.html':
        if 'BetterHelp' not in content:
            failures.append(f'[{fname}] MISSING: BetterHelp in affiliate programs list')
        if 'Talkspace' not in content:
            failures.append(f'[{fname}] MISSING: Talkspace in affiliate programs list')

for fname in html_files:
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    check(fname, content)

print(f'Quality gate: {len(html_files)} pages checked')
print()
if failures:
    print(f'FAILURES ({len(failures)}):')
    for f in failures:
        print(f'  {f}')
else:
    print('ALL CHECKS PASSED - no failures')
print()
if warnings:
    print(f'WARNINGS ({len(warnings)}):')
    for w in warnings:
        print(f'  {w}')
else:
    print('No warnings')
