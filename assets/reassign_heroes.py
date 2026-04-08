import os, re

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

# Pages where hero-calm (gentle smile, warm light) fits better than hero-emotional (back-to-window)
calm_pages = {
    'stress.html', 'burnout.html', 'life-transitions.html',
    'self-esteem.html', 'loneliness.html', 'insomnia.html',
}

count = 0
for fname in os.listdir(output_dir):
    if not fname.endswith('.html') or fname not in calm_pages:
        continue
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'hero-emotional.webp' in content:
        new_content = content.replace('../assets/hero-emotional.webp', '../assets/hero-calm.webp')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f'  Reassigned: {fname}')

print(f'\nDone: {count} pages now use hero-calm.webp')
print(f'Remaining hero-emotional pages: condition pages with higher emotional weight')
