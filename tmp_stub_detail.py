import sys
sys.stdout.reconfigure(encoding='utf-8')
with open(r'D:\Work\Digital-Therapy-Solutions\output\conditions.html', encoding='utf-8') as f:
    lines = f.readlines()
# Print lines 248-310
for i, line in enumerate(lines[247:310], start=248):
    print(f'{i}: {line}', end='')
