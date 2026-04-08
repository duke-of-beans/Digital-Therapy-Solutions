import os, re

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

skip = {'about.html', 'editorial-policy.html', 'affiliate-disclosure.html',
        'privacy-policy.html', 'crisis-resources.html', 'how-online-therapy-works.html',
        'do-i-need-therapy.html', 'index.html', 'reviews.html', 'conditions.html', 'insurance.html'}

disclosure = '<p class="cta-disclosure">Affiliate link &mdash; we may earn a commission if you sign up, at no extra cost to you.</p>'

count_files = 0
count_insertions = 0

for fname in os.listdir(output_dir):
    if not fname.endswith('.html') or fname in skip:
        continue
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    already = content.count('cta-disclosure')

    # Pattern 1: inside platform-card__cta, before the cta-button link
    # Handles optional offer-tag span
    new_content = re.sub(
        r'(<div class="platform-card__cta">)((?:\s*<span class="offer-tag">[^<]*</span>)?\s*)(<a [^>]*class="cta-button)',
        lambda m: m.group(1) + m.group(2) + '\n' + disclosure + '\n' + m.group(3),
        content
    )

    # Pattern 2: standalone pending CTA outside platform-card__cta (verdict section on review pages)
    new_content = re.sub(
        r'\n(<a [^>]*class="cta-button cta-button--pending")',
        '\n' + disclosure + '\n' + r'\1',
        new_content
    )

    after = new_content.count('cta-disclosure')
    insertions = after - already

    if insertions > 0:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count_files += 1
        count_insertions += insertions

print(f'FTC disclosure: {count_insertions} insertions across {count_files} files')
