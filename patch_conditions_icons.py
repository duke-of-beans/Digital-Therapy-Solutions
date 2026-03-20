import sys, re
sys.stdout.reconfigure(encoding='utf-8')

# SVG icon map: emoji/entity → inline SVG
# All: stroke-based, humanist, var(--accent-primary), viewBox 32x32
S = 'stroke="var(--accent-primary)"'
A = 'fill="none"'
L = 'stroke-linecap="round" stroke-linejoin="round"'
W = 'stroke-width="1.8"'
def svg(paths): return f'<svg viewBox="0 0 32 32" {A} {S} {W} {L}>{paths}</svg>'

ICONS = {
    # Anxiety (😰 wavy lines)
    '😰': svg('<path d="M4 20 Q8 14 12 20 Q16 26 20 20 Q24 14 28 20"/><path d="M4 13 Q8 7 12 13 Q16 19 20 13 Q24 7 28 13"/>'),
    # Depression (🌧️ rain cloud)
    '🌧️': svg('<path d="M10 18 Q8 12 12 10 Q12 6 18 6 Q24 6 24 12 Q28 12 28 17 Q28 20 24 20 L10 20 Q6 20 6 17 Q6 14 10 18Z"/><path d="M12 23 L11 26"/><path d="M16 23 L15 26"/><path d="M20 23 L19 26"/>'),
    # ADHD (⚡ lightning bolt)
    '⚡': svg('<path d="M18 4 L12 16 L20 16 L14 28"/>'),
    # Couples (💑 two interlocking circles)
    '💑': svg('<circle cx="11" cy="16" r="7"/><circle cx="21" cy="16" r="7"/>'),
    # OCD (🔁 loop arrow)
    '🔁': svg('<path d="M8 20 Q8 26 16 26 Q24 26 24 20 Q24 14 16 14"/><path d="M12 10 L16 14 L12 18"/>'),
    # PTSD/Trauma (🛡️ shield)
    '🛡️': svg('<path d="M16 3 L5 7 L5 16 Q5 23 16 29 Q27 23 27 16 L27 7 Z"/>'),
    # Bipolar (📊 dual arc wave)
    '📊': svg('<path d="M4 20 Q8 6 16 16 Q24 26 28 12"/>'),
    # Eating Disorders (🥗 leaf/scale)
    '🥗': svg('<path d="M16 28 Q16 16 8 10 Q16 10 24 16 Q16 16 16 28Z"/>'),
    # Grief (🕊️ teardrop)
    '🕊️': svg('<path d="M16 6 Q22 12 22 18 Q22 24 16 26 Q10 24 10 18 Q10 12 16 6Z"/>'),
    # Addiction (🔗 broken chain)
    '🔗': svg('<path d="M10 16 L8 18 Q6 20 8 22 Q10 24 12 22 L14 20"/><path d="M18 16 L20 14 Q22 12 20 10 Q18 8 16 10 L14 12"/><path d="M14 12 L14 20" stroke-dasharray="3 3"/>'),
    # Stress (🌋 spiral)
    '🌋': svg('<path d="M16 16 Q16 10 22 10 Q28 10 28 16 Q28 22 22 22 Q14 22 14 14 Q14 8 20 8 Q26 8 26 14"/>'),
    # Burnout (🔥 candle extinguished)
    '🔥': svg('<line x1="16" y1="8" x2="16" y2="24"/><path d="M12 24 Q16 26 20 24"/><path d="M14 8 Q16 6 18 8"/><path d="M12 10 Q13 6 16 4" stroke-dasharray="2 3"/>'),
    # Relationship (🪟 tangled knot)
    '🪟': svg('<path d="M10 22 Q8 16 12 12 Q16 8 20 12 Q24 16 20 20 Q16 24 12 20 Q10 17 14 14 Q18 11 20 16"/>'),
    # LGBTQ+ (🏳️‍🌈 interlocking rings)
    '🏳️‍🌈': svg('<circle cx="12" cy="16" r="6"/><circle cx="20" cy="16" r="6"/>'),
    # Teen (🎒 sprout/seedling)
    '🎒': svg('<path d="M16 26 L16 16"/><path d="M16 16 Q16 10 10 10 Q10 16 16 16"/><path d="M16 16 Q16 10 22 10 Q22 16 16 16"/>'),
    # Postpartum (🤱 gentle arc/cradle)
    '🤱': svg('<path d="M6 22 Q6 14 16 14 Q26 14 26 22"/><path d="M10 22 Q10 18 16 18 Q22 18 22 22"/><circle cx="16" cy="10" r="3"/>'),
    # Insomnia (🌙 crescent + star)
    '🌙': svg('<path d="M20 8 Q14 8 10 14 Q6 20 10 24 Q16 28 22 24 Q26 22 26 18 Q22 20 18 18 Q14 14 16 10 Q18 8 20 8Z"/><circle cx="26" cy="10" r="1.5" fill="var(--accent-primary)" stroke="none"/>'),
    # Chronic Pain (🩺 wave + body)
    '🩺': svg('<path d="M4 20 Q8 14 12 20 Q16 26 20 20 Q24 14 28 20"/><line x1="16" y1="4" x2="16" y2="12"/>'),
    # Social Anxiety (🤝 single figure with space)
    '🤝': svg('<circle cx="16" cy="9" r="4"/><path d="M8 28 Q8 20 16 20 Q24 20 24 28"/><circle cx="7" cy="16" r="2" stroke-dasharray="2 2"/><circle cx="25" cy="16" r="2" stroke-dasharray="2 2"/>'),
    # Phobias (🧔 eye looking away)
    '🧔': svg('<ellipse cx="16" cy="16" rx="12" ry="7"/><circle cx="20" cy="16" r="4"/><circle cx="21" cy="15" r="1.5" fill="var(--accent-primary)" stroke="none"/>'),
    # Panic (&#x1F4A8; expanding circles)
    '&#x1F4A8;': svg('<circle cx="16" cy="16" r="3"/><circle cx="16" cy="16" r="7"/><circle cx="16" cy="16" r="12"/>'),
    # Loneliness (🧭 single figure)
    '🧭': svg('<circle cx="16" cy="10" r="4"/><path d="M10 28 Q10 20 16 20 Q22 20 22 28"/>'),
    # Self-Esteem (🧩 upward arrow/star)
    '🧩': svg('<path d="M16 6 L18.5 13 L26 13 L20 17.5 L22.5 24.5 L16 20 L9.5 24.5 L12 17.5 L6 13 L13.5 13 Z"/>'),
    # Anger (&#x1F525; flame)
    '&#x1F525;': svg('<path d="M16 28 Q8 24 8 17 Q8 12 14 10 Q12 14 16 14 Q14 10 18 6 Q22 12 22 17 Q22 24 16 28Z"/>'),
    # Stress 2 (&#x1F610; expressionless — neutral face for stress/numbness)
    '&#x1F610;': svg('<circle cx="16" cy="16" r="11"/><line x1="11" y1="19" x2="21" y2="19"/><circle cx="12" cy="13" r="1.5" fill="var(--accent-primary)" stroke="none"/><circle cx="20" cy="13" r="1.5" fill="var(--accent-primary)" stroke="none"/>'),
    # Chronic pain 2 (&#x26A0;&#xFE0F; ⚠ — warning triangle for pain)
    '&#x26A0;&#xFE0F;': svg('<path d="M16 6 L28 26 L4 26 Z"/><line x1="16" y1="14" x2="16" y2="20"/><circle cx="16" cy="23" r="1" fill="var(--accent-primary)" stroke="none"/>'),
    # Life transitions (🧩)
    '🧩': svg('<rect x="6" y="6" width="8" height="8" rx="2"/><rect x="18" y="6" width="8" height="8" rx="2"/><rect x="6" y="18" width="8" height="8" rx="2"/><rect x="18" y="18" width="8" height="8" rx="2"/>'),
    # Self-harm/relationships (💜 heart)
    '💜': svg('<path d="M16 26 Q6 18 6 12 Q6 6 12 6 Q15 6 16 9 Q17 6 20 6 Q26 6 26 12 Q26 18 16 26Z"/>'),
    # Mens mental health (🧔 male figure)
    '🧔': svg('<circle cx="16" cy="10" r="5"/><path d="M9 28 Q9 20 16 20 Q23 20 23 28"/><path d="M13 9 Q13 7 16 7 Q19 7 19 9" stroke-width="1.2"/>'),
}

with open(r'D:\Work\Digital-Therapy-Solutions\output\conditions.html', 'r', encoding='utf-8') as f:
    html = f.read()

count = 0
for emoji, svg_html in ICONS.items():
    old = f'<div style="font-size:2rem;">{emoji}</div>'
    new = f'<div class="condition-tile__icon">{svg_html}</div>'
    if old in html:
        html = html.replace(old, new)
        count += 1
        print(f'  Replaced: {emoji}')

print(f'Total replacements: {count}')

with open(r'D:\Work\Digital-Therapy-Solutions\output\conditions.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done.')
