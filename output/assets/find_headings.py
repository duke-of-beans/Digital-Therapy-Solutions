import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
import re

for slug in ['bcbs', 'cigna']:
    f = Path(r'D:\Work\Digital-Therapy-Solutions\output') / f'{slug}.html'
    txt = f.read_text(encoding='utf-8')
    # Find all section-headings
    for m in re.finditer(r'<h2 class="section-heading">(.*?)</h2>', txt):
        print(f'{slug}: {m.group(1)}')
