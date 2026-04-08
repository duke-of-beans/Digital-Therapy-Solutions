import os

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

replacements = [
    # Pattern from condition/review pages
    ('<a class="link-subtle" href="#">Read our editorial policy \u2192</a>',
     '<a class="link-subtle" href="editorial-policy.html#editorial-team">Read our editorial process \u2192</a>'),
    # Alternate pattern (seen in some review pages)
    ('<a class="link-subtle" href="#">View full bio \u2192</a>',
     '<a class="link-subtle" href="editorial-policy.html#editorial-team">Read our editorial process \u2192</a>'),
    # Arrow as HTML entity variants
    ('<a class="link-subtle" href="#">Read our editorial policy &#x2192;</a>',
     '<a class="link-subtle" href="editorial-policy.html#editorial-team">Read our editorial process &#x2192;</a>'),
    ('<a class="link-subtle" href="#">View full bio &#x2192;</a>',
     '<a class="link-subtle" href="editorial-policy.html#editorial-team">Read our editorial process &#x2192;</a>'),
    # Anchor-only href="#" on See full review links in reviewer card meta
    ('<a href="#">See full review \u2192</a>',
     '<a href="editorial-policy.html#editorial-team">See full review \u2192</a>'),
]

count = 0
for fname in os.listdir(output_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    for old, new in replacements:
        content = content.replace(old, new)
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f'Reviewer/editorial links fixed on {count} pages')
