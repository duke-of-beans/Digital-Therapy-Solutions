import re
with open(r'D:\Work\Digital-Therapy-Solutions\output\templates\styles.css', encoding='utf-8') as f:
    css = f.read()

patterns = {
    'visual-break': r'\.visual-break\s*\{[^}]+\}',
    'visual-break__image': r'\.visual-break__image\s*\{[^}]+\}',
    'visual-break__overlay': r'\.visual-break__overlay\s*\{[^}]+\}',
    'visual-break__text': r'\.visual-break__text\s*\{[^}]+\}',
    'visual-break__quote': r'\.visual-break__quote\s*\{[^}]+\}',
    'hero-image': r'\.hero-image\s*\{[^}]+\}',
    'hero-visual': r'\.hero-visual\s*\{[^}]+\}',
    'reveal': r'\s\.reveal\s*\{[^}]+\}',
}
for name, pat in patterns.items():
    m = re.search(pat, css, re.DOTALL)
    if m:
        print(f'=== {name} ===')
        print(m.group()[:500])
        print()
    else:
        print(f'=== {name} === NOT FOUND\n')
