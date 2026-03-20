import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
with open('output/aetna.html', encoding='utf-8', errors='ignore') as f:
    content = f.read()
matches = re.findall(r'.{0,30}[\U0001F300-\U0001FFFF\U00002600-\U000027FF\u2714\u2716\u2728\u2705\u274C\u2726\u2736\u2756].{0,30}', content)
for m in matches[:10]:
    print(repr(m))
