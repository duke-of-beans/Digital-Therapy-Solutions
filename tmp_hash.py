import sys
sys.stdout.reconfigure(encoding='utf-8')
with open(r'D:\Work\Digital-Therapy-Solutions\STATUS.md', encoding='utf-8') as f:
    c = f.read()
c = c.replace('| PS-CONDITIONS-02 | 4 remaining condition pages | \u2705 COMPLETE | TBD |',
              '| PS-CONDITIONS-02 | 4 remaining condition pages | \u2705 COMPLETE | 16ad1e8 |')
with open(r'D:\Work\Digital-Therapy-Solutions\STATUS.md', 'w', encoding='utf-8') as f:
    f.write(c)
print('hash written')
