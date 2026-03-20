import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'D:\Work\Digital-Therapy-Solutions\STATUS.md', encoding='utf-8') as f:
    content = f.read()

# Update sprint row
content = content.replace(
    '| PS-CONDITIONS-02 | 4 remaining stub condition pages | ⬜ QUEUED | — |',
    '| PS-CONDITIONS-02 | 4 remaining condition pages | ✅ COMPLETE | TBD |'
)

# Update Last Updated
content = content.replace(
    'Last Updated: 2026-03-19',
    'Last Updated: 2026-03-20'
)

# Update Conditions inventory
content = content.replace(
    '### Conditions (24 live + 4 stubs / 28 total)',
    '### Conditions (28 live / 28 total) ✅ COMPLETE'
)
content = content.replace(
    '- [ ] mens-mental-health.html (slug confirmed)',
    '- [x] mens-mental-health.html'
)
content = content.replace(
    '- [ ] womens-mental-health.html (slug confirmed)',
    '- [x] womens-mental-health.html'
)
content = content.replace(
    '- [ ] life-transitions.html (slug confirmed)',
    '- [x] life-transitions.html'
)
content = content.replace(
    '- [ ] autism.html (slug confirmed)',
    '- [x] autism.html'
)

with open(r'D:\Work\Digital-Therapy-Solutions\STATUS.md', 'w', encoding='utf-8') as f:
    f.write(content)
print('STATUS.md updated OK')
