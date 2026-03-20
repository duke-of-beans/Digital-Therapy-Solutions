import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')
css = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/templates/styles.css').read_text(encoding='utf-8')
# Find all occurrences of condition-tile__icon svg rule
matches = [(m.start(), m.group()) for m in re.finditer(r'\.condition-tile__icon svg\s*\{[^}]+\}', css)]
for pos, match in matches:
    line = css[:pos].count('\n') + 1
    print(f"Line {line}: {match[:100]}")
