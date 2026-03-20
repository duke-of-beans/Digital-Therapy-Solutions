import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'D:\Work\Digital-Therapy-Solutions\output\conditions.html', encoding='utf-8') as f:
    content = f.read()

# ---- Men's Mental Health stub -> live card ----
old_mens = '''                    <!-- STUB: Men's Mental Health -->
                    <div class="hub-card hub-card--stub">
                        <div class="condition-tile__icon"><svg viewBox="0 0 32 32" fill="none" stroke="var(--accent-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="16" cy="10" r="5"/><path d="M9 28 Q9 20 16 20 Q23 20 23 28"/><path d="M13 9 Q13 7 16 7 Q19 7 19 9" stroke-width="1.2"/></svg></div>
                        <div class="hub-card__name">Men\'s Mental Health</div>
                        <div class="hub-card__desc">Overcoming stigma and finding the right therapeutic fit</div>
                        <span class="hub-card__cta">Guide Coming</span>
                    </div>'''

new_mens = '''                    <!-- Men's Mental Health -->
                    <a href="mens-mental-health.html" class="hub-card">
                        <div class="condition-tile__icon"><svg viewBox="0 0 32 32" fill="none" stroke="var(--accent-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="16" cy="10" r="5"/><path d="M8 28 Q8 20 16 20 Q24 20 24 28"/><path d="M20 8 L24 4 M22 12 L27 11"/></svg></div>
                        <div class="hub-card__name">Men\'s Mental Health</div>
                        <div class="hub-card__desc">Overcoming stigma and finding the right therapeutic fit</div>
                        <span class="hub-card__cta">Read Guide &rarr;</span>
                    </a>'''

# ---- Women's Mental Health stub -> live card ----
old_womens = '''                    <!-- STUB: Women's Mental Health -->
                    <div class="hub-card hub-card--stub">
                        <div class="condition-tile__icon"><svg viewBox="0 0 32 32" fill="none" stroke="var(--accent-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M16 26 Q6 18 6 12 Q6 6 12 6 Q15 6 16 9 Q17 6 20 6 Q26 6 26 12 Q26 18 16 26Z"/></svg></div>
                        <div class="hub-card__name">Women\'s Mental Health</div>
                        <div class="hub-card__desc">Hormonal, relational, and identity-focused care for women</div>
                        <span class="hub-card__cta">Guide Coming</span>
                    </div>'''

new_womens = '''                    <!-- Women's Mental Health -->
                    <a href="womens-mental-health.html" class="hub-card">
                        <div class="condition-tile__icon"><svg viewBox="0 0 32 32" fill="none" stroke="var(--accent-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="16" cy="12" r="7"/><path d="M16 19 L16 28"/><path d="M12 24 L20 24"/></svg></div>
                        <div class="hub-card__name">Women\'s Mental Health</div>
                        <div class="hub-card__desc">Hormonal, relational, and identity-focused care for women</div>
                        <span class="hub-card__cta">Read Guide &rarr;</span>
                    </a>'''

# ---- Life Transitions stub -> live card ----
old_life = '''                    <!-- STUB: Life Transitions -->
                    <div class="hub-card hub-card--stub">
                        <div class="condition-tile__icon"><svg viewBox="0 0 32 32" fill="none" stroke="var(--accent-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="16" cy="10" r="4"/><path d="M10 28 Q10 20 16 20 Q22 20 22 28"/></svg></div>
                        <div class="hub-card__name">Life Transitions</div>
                        <div class="hub-card__desc">Navigating career changes, moves, divorce, and identity shifts</div>
                        <span class="hub-card__cta">Guide Coming</span>
                    </div>'''

new_life = '''                    <!-- Life Transitions -->
                    <a href="life-transitions.html" class="hub-card">
                        <div class="condition-tile__icon"><svg viewBox="0 0 32 32" fill="none" stroke="var(--accent-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 24 Q10 8 16 16 Q22 24 28 8"/><path d="M24 8 L28 8 L28 12"/></svg></div>
                        <div class="hub-card__name">Life Transitions</div>
                        <div class="hub-card__desc">Navigating career changes, moves, divorce, and identity shifts</div>
                        <span class="hub-card__cta">Read Guide &rarr;</span>
                    </a>'''

# ---- Autism & Neurodivergence stub -> live card ----
old_autism = '''                    <!-- STUB: Autism & Neurodivergence -->
                    <div class="hub-card hub-card--stub">
                        <div class="condition-tile__icon"><svg viewBox="0 0 32 32" fill="none" stroke="var(--accent-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="6" width="8" height="8" rx="2"/><rect x="18" y="6" width="8" height="8" rx="2"/><rect x="6" y="18" width="8" height="8" rx="2"/><rect x="18" y="18" width="8" height="8" rx="2"/></svg></div>
                        <div class="hub-card__name">Autism &amp; Neurodivergence</div>
                        <div class="hub-card__desc">Therapists experienced with ASD, sensory needs, and masking</div>
                        <span class="hub-card__cta">Guide Coming</span>
                    </div>'''

new_autism = '''                    <!-- Autism & Neurodivergence -->
                    <a href="autism.html" class="hub-card">
                        <div class="condition-tile__icon"><svg viewBox="0 0 32 32" fill="none" stroke="var(--accent-primary)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="16" cy="16" r="4"/><circle cx="16" cy="16" r="9"/><path d="M16 7 L16 4"/><path d="M16 28 L16 25"/><path d="M7 16 L4 16"/><path d="M28 16 L25 16"/></svg></div>
                        <div class="hub-card__name">Autism &amp; Neurodivergence</div>
                        <div class="hub-card__desc">Therapists experienced with ASD, sensory needs, and masking</div>
                        <span class="hub-card__cta">Read Guide &rarr;</span>
                    </a>'''

replacements = [
    (old_mens, new_mens, "Men's Mental Health"),
    (old_womens, new_womens, "Women's Mental Health"),
    (old_life, new_life, "Life Transitions"),
    (old_autism, new_autism, "Autism & Neurodivergence"),
]

for old, new, label in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f'[OK] Replaced: {label}')
    else:
        print(f'[MISS] Not found: {label}')

with open(r'D:\Work\Digital-Therapy-Solutions\output\conditions.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('conditions.html patched.')
