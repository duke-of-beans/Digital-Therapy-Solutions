import os, re

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

clr_files = []
for fname in os.listdir(output_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'clr-primary' in content:
        count = content.count('clr-primary')
        clr_files.append((fname, count))

print(f'Files with clr-primary: {len(clr_files)}')
for f, c in clr_files:
    print(f'  {f}: {c} occurrences')
