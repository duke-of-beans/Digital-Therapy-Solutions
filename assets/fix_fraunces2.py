import os

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

# Remove Fraunces from any remaining pages (about/editorial-policy had a slightly different string)
old_variants = [
    'family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=',
    'family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600&amp;',
]

count = 0
for fname in os.listdir(output_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    for old in old_variants:
        content = content.replace(old, 'family=')
    # Clean up double "family=" if both patterns somehow hit
    content = content.replace('family=family=', 'family=')
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'  Cleaned: {fname}')

print(f'Fraunces remnants removed from {count} additional files')
