import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
import re

OUTPUT_DIR = Path(r'D:\Work\Digital-Therapy-Solutions\output')

STAT_BLOCK_BCBS = '''<div class="split-section reveal">
<div class="split-section__main">
{inner}
</div>
<div class="split-section__aside">
<div class="stat-callout">
<div class="stat-callout__number">$15</div>
<div class="stat-callout__label">avg copay with BCBS in-network</div>
</div>
</div>
</div>'''

FEATURE_LIST_CIGNA = '''<p>Not every Cigna plan works with every platform. If you get a "not covered" result, you still have options:</p>
<div class="feature-list reveal">
<div class="feature-list__item">
<svg class="feature-list__icon feature-list__icon--positive" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>
<div class="feature-list__content">
<div class="feature-list__title">Out-of-network reimbursement</div>
<div class="feature-list__desc">Many Cigna OAP plans cover out-of-network mental health at 50–70% after deductible. Pay upfront, submit a claim for partial reimbursement. Call the number on the back of your card to check your out-of-network mental health benefits.</div>
</div>
</div>
<div class="feature-list__item">
<svg class="feature-list__icon feature-list__icon--positive" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>
<div class="feature-list__content">
<div class="feature-list__title">Cigna EAP</div>
<div class="feature-list__desc">Even if your therapy coverage is limited, your employer\'s EAP through Cigna may offer free sessions — typically 3–8 — as a separate benefit that doesn\'t require meeting a deductible.</div>
</div>
</div>
<div class="feature-list__item">
<svg class="feature-list__icon feature-list__icon--positive" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>
<div class="feature-list__content">
<div class="feature-list__title">Financial assistance programs</div>
<div class="feature-list__desc">BetterHelp offers financial aid that can reduce costs by 10–40%. Calmerry starts at $42/week without insurance. Both are affordable alternatives when insurance doesn\'t apply.</div>
</div>
</div>
<div class="feature-list__item">
<svg class="feature-list__icon feature-list__icon--positive" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>
<div class="feature-list__content">
<div class="feature-list__title">Affordable self-pay alternatives</div>
<div class="feature-list__desc">See our <a href="affordable.html">guide to affordable online therapy</a> for platforms starting at $30/session with no insurance required.</div>
</div>
</div>
</div>'''

# --- PATCH BCBS: coverage section ---
bcbs_path = OUTPUT_DIR / 'bcbs.html'
bcbs = bcbs_path.read_text(encoding='utf-8')

# Find the coverage section's inner <div class="reveal">...</div>
pattern = r'(<h2 class="section-heading">How Blue Cross Blue Shield Coverage Works[^<]*</h2>\s*)<div class="reveal">(.*?)</div>\s*(?=</div>\s*</div>)'
def replace_bcbs_coverage(m):
    inner = f'<div class="reveal">{m.group(2)}</div>'
    block = STAT_BLOCK_BCBS.format(inner=inner)
    return m.group(1) + block
new_bcbs, n = re.subn(pattern, replace_bcbs_coverage, bcbs, flags=re.DOTALL)
if n:
    bcbs_path.write_text(new_bcbs, encoding='utf-8')
    print(f'PATCHED bcbs coverage section ({n}x)')
else:
    print('WARN: bcbs coverage pattern not matched')
    # Debug: show surrounding context
    idx = bcbs.find('How Blue Cross Blue Shield Coverage Works')
    if idx >= 0:
        print('Context:', repr(bcbs[idx:idx+300]))

# --- PATCH CIGNA: whatif section ---
cigna_path = OUTPUT_DIR / 'cigna.html'
cigna = cigna_path.read_text(encoding='utf-8')

pattern2 = r"(<h2 class=\"section-heading\">What If My Plan Isn't Accepted\?</h2>\s*)<div class=\"reveal\">(.*?)</div>\s*(?=</div>\s*</div>)"
def replace_cigna_whatif(m):
    return m.group(1) + FEATURE_LIST_CIGNA
new_cigna, n2 = re.subn(pattern2, replace_cigna_whatif, cigna, flags=re.DOTALL)
if n2:
    cigna_path.write_text(new_cigna, encoding='utf-8')
    print(f'PATCHED cigna whatif section ({n2}x)')
else:
    print('WARN: cigna whatif pattern not matched')
    idx = cigna.find("What If My Plan")
    if idx >= 0:
        print('Context:', repr(cigna[idx:idx+400]))

print('Done.')
