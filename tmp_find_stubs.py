import sys
sys.stdout.reconfigure(encoding='utf-8')
with open(r'D:\Work\Digital-Therapy-Solutions\output\conditions.html', encoding='utf-8') as f:
    lines = f.readlines()
keywords = ["Men", "Women", "Life Trans", "Autism", "stub", "mens-mental", "womens-mental", "life-trans", "autism"]
for i, line in enumerate(lines):
    if any(x.lower() in line.lower() for x in keywords):
        print(f'{i+1}: {line}', end='')
