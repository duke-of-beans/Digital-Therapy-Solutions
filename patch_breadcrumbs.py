"""
patch_breadcrumbs.py — PS-HUB-01
Inserts breadcrumb nav just after <main id="main-content"> on
condition, review, and insurance pages.
"""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

# Map filename -> breadcrumb trail
BREADCRUMBS = {
    # Conditions
    'anxiety.html':     '<a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="conditions.html">Conditions</a><span class="breadcrumb__sep">/</span>Anxiety',
    'depression.html':  '<a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="conditions.html">Conditions</a><span class="breadcrumb__sep">/</span>Depression',
    'adhd.html':        '<a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="conditions.html">Conditions</a><span class="breadcrumb__sep">/</span>ADHD',
    'couples.html':     '<a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="conditions.html">Conditions</a><span class="breadcrumb__sep">/</span>Couples Therapy',
    # Reviews
    'betterhelp-review.html':        '<a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="reviews.html">Reviews</a><span class="breadcrumb__sep">/</span>BetterHelp',
    'talkspace-review.html':         '<a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="reviews.html">Reviews</a><span class="breadcrumb__sep">/</span>Talkspace',
    'online-therapy-com-review.html':'<a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="reviews.html">Reviews</a><span class="breadcrumb__sep">/</span>Online-Therapy.com',
    # Insurance
    'aetna.html':            '<a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="insurance.html">Insurance</a><span class="breadcrumb__sep">/</span>Aetna',
    'bcbs.html':             '<a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="insurance.html">Insurance</a><span class="breadcrumb__sep">/</span>Blue Cross Blue Shield',
    'cigna.html':            '<a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="insurance.html">Insurance</a><span class="breadcrumb__sep">/</span>Cigna',
    'unitedhealthcare.html': '<a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="insurance.html">Insurance</a><span class="breadcrumb__sep">/</span>UnitedHealthcare',
    'medicaid.html':         '<a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="insurance.html">Insurance</a><span class="breadcrumb__sep">/</span>Medicaid',
    'affordable.html':       '<a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="insurance.html">Insurance</a><span class="breadcrumb__sep">/</span>Paying Out of Pocket',
}

MAIN_ANCHOR = '<main id="main-content">'

changed = []
skipped = []
already = []

for fname, crumb_inner in BREADCRUMBS.items():
    fpath = os.path.join(output_dir, fname)
    if not os.path.exists(fpath):
        skipped.append(f'{fname} (not found)')
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'class="breadcrumb"' in content:
        already.append(fname)
        continue

    breadcrumb_html = (
        f'\n\n    <nav aria-label="Breadcrumb" class="breadcrumb" style="max-width:var(--table-width);margin:0 auto;padding:var(--space-xs) var(--space-md);">\n'
        f'        {crumb_inner}\n'
        f'    </nav>'
    )

    new_content = content.replace(MAIN_ANCHOR, MAIN_ANCHOR + breadcrumb_html, 1)

    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        changed.append(fname)
    else:
        skipped.append(f'{fname} (anchor not found)')

print(f'Breadcrumbs added ({len(changed)}):')
for f in changed: print(f'  ✅ {f}')
if already:
    print(f'\nAlready had breadcrumb ({len(already)}):')
    for f in already: print(f'  — {f}')
if skipped:
    print(f'\nSkipped ({len(skipped)}):')
    for f in skipped: print(f'  ⚠ {f}')
