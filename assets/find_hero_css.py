import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')
css = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/templates/styles.css').read_text(encoding='utf-8')
matches = [(m.start(), m.group()) for m in re.finditer(r'\.hero-subhead\s*\{[^}]+\}', css)]
for pos, m in matches:
    line = css[:pos].count('\n') + 1
    print(f"Line {line}: {m[:200]}")
    print('---')
