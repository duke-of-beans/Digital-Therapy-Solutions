import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'D:\Work\Digital-Therapy-Solutions\output\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# SVG icons for each condition — stroke-based, humanist style, 32x32 viewBox
icons = {
    'anxiety': '<svg viewBox="0 0 32 32" fill="none" stroke="var(--accent-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20 Q8 14 12 20 Q16 26 20 20 Q24 14 28 20"/><path d="M4 13 Q8 7 12 13 Q16 19 20 13 Q24 7 28 13"/></svg>',
    'depression': '<svg viewBox="0 0 32 32" fill="none" stroke="var(--accent-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M8 26 Q16 6 24 26"/><path d="M6 22 Q10 18 16 17 Q22 18 26 22"/><circle cx="16" cy="10" r="2"/></svg>',
    'adhd': '<svg viewBox="0 0 32 32" fill="none" stroke="var(--accent-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4 L12 16 L20 16 L14 28"/></svg>',
    'couples': '<svg viewBox="0 0 32 32" fill="none" stroke="var(--accent-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="16" r="7"/><circle cx="21" cy="16" r="7"/></svg>',
}

# Replace emoji icons in the 4 condition tiles
replacements = [
    ('<div class="condition-tile__icon">🌊</div>', f'<div class="condition-tile__icon">{icons["anxiety"]}</div>'),
    ('<div class="condition-tile__icon">☁️</div>', f'<div class="condition-tile__icon">{icons["depression"]}</div>'),
    ('<div class="condition-tile__icon">⚡</div>', f'<div class="condition-tile__icon">{icons["adhd"]}</div>'),
    ('<div class="condition-tile__icon">💑</div>', f'<div class="condition-tile__icon">{icons["couples"]}</div>'),
]

for old, new in replacements:
    if old in html:
        html = html.replace(old, new)
        print(f'  Replaced: {old[:40]}...')
    else:
        print(f'  NOT FOUND: {old[:40]}...')

with open(r'D:\Work\Digital-Therapy-Solutions\output\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done patching index.html emoji icons.')
