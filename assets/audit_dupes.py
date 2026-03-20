import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')

path = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/templates/styles.css')
css = path.read_text(encoding='utf-8')

# For each duplicate, show all occurrences with line numbers so we can decide what to keep
targets = [
    '.hero-subhead--follow',
    '.trust-row',
    '.condition-tile__icon',
    '.platform-card__logo img',
    '.insurance-tile__logo',
]

for sel in targets:
    pattern = re.compile(r'(' + re.escape(sel) + r'\s*\{[^}]*\})', re.DOTALL)
    matches = list(pattern.finditer(css))
    print(f"\n{'='*60}")
    print(f"SELECTOR: {sel} ({len(matches)} occurrences)")
    for i, m in enumerate(matches):
        line = css[:m.start()].count('\n') + 1
        print(f"\n  [{i+1}] Line {line}:")
        print('  ' + m.group()[:200])
