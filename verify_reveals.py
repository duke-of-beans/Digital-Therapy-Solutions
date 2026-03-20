import os, re
import sys
sys.stdout.reconfigure(encoding='utf-8')

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

# Verify .reveal warnings are false positives
for fname in ['anxiety.html', 'about.html', 'index.html', 'do-i-need-therapy.html']:
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    count = len(re.findall(r'reveal', content))
    print(f'{fname}: {count} occurrences of "reveal"')
