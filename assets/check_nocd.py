with open('output/nocd-review.html', encoding='utf-8') as f:
    c = f.read()
checks = [
    ('feature-list__title', c.count('feature-list__title')),
    ('visual-break', c.count('visual-break')),
    ('comparison-table', c.count('comparison-table')),
    ('split-section', c.count('split-section')),
    ('pull-quote', c.count('pull-quote')),
    ('cta-disclosure', c.count('cta-disclosure')),
    ('editorial-team', c.count('editorial-team')),
    ('Fraunces', c.count('Fraunces')),
]
for name, count in checks:
    status = 'OK' if (count > 0 if name != 'Fraunces' else count == 0) else 'FAIL'
    print(f'{status} {name}: {count}')
print(f'Total chars: {len(c)}')
