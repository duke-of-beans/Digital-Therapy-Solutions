import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')
html = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/affordable.html').read_text(encoding='utf-8')
# Find all logo wrapper patterns
matches = re.finditer(r'<div class="logo"[^>]*>.*?</div>', html, re.DOTALL)
for m in matches:
    print(m.group()[:300])
    print('---')
