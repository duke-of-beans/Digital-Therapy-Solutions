import os

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'
old = 'family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600&amp;'
new = ''

count = 0
for fname in os.listdir(output_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f'Fraunces removed from {count} files')
