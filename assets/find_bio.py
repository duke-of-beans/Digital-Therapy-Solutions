import os

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

# Find any remaining href="#" in platform-card__meta sections
found = []
for fname in os.listdir(output_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    idx = content.find('platform-card__meta')
    if idx != -1:
        block = content[idx:idx+300]
        if 'href="#"' in block:
            found.append(fname)
            print(repr(block))
            print()
            if len(found) >= 2:
                break

if not found:
    print('No href="#" found in platform-card__meta sections')
