import re
with open('D:/Work/Digital-Therapy-Solutions/templates/styles.css', encoding='utf-8') as f:
    content = f.read()
matches = [(m.start(), content[max(0,m.start()-50):m.start()+150]) for m in re.finditer(r'hub-card|text-decoration', content)]
for pos, ctx in matches[:30]:
    print(f'Line ~{content[:pos].count(chr(10))}: {ctx.strip()[:150]}')
    print('---')
