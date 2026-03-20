import sys
sys.stdout.reconfigure(encoding='utf-8')
lines = open(r'D:\Work\Digital-Therapy-Solutions\templates\styles.css', encoding='utf-8').readlines()
for i, l in enumerate(lines[2180:2210], start=2181):
    print(f'{i}: {l}', end='')
