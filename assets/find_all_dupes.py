import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')
css = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/templates/styles.css').read_text(encoding='utf-8')

# Find all duplicate selectors
selectors = re.findall(r'^(\.[a-z][a-z0-9_-]*(?:\s+[a-z][a-z0-9_-]*)?)\s*\{', css, re.MULTILINE)
from collections import Counter
dupes = {k: v for k, v in Counter(selectors).items() if v > 1}
print("DUPLICATE SELECTORS:")
for sel, count in sorted(dupes.items(), key=lambda x: -x[1]):
    print(f"  {count}x  {sel}")
