import re
with open(r'D:\Work\Digital-Therapy-Solutions\output\templates\styles.css', encoding='utf-8') as f:
    css = f.read()

patterns = {
    'cta-button': r'\.cta-button\s*\{[^}]+\}',
    'score-number': r'\.score-number\s*\{[^}]+\}',
    'stat-callout__number': r'\.stat-callout__number\s*\{[^}]+\}',
    'table-mono': r'\.table-mono\s*\{[^}]+\}',
}
for name, pat in patterns.items():
    m = re.search(pat, css, re.DOTALL)
    if m:
        print(f'=== {name} ===')
        print(m.group()[:400])
        print()
    else:
        print(f'=== {name} === NOT FOUND')
        print()
