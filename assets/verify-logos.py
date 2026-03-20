import sys, os
sys.stdout.reconfigure(encoding='utf-8')

from PIL import Image

LOGOS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logos')
OUTPUT    = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'LOGO_AUDIT.md')

results = []
flagged = 0

for fname in sorted(os.listdir(LOGOS_DIR)):
    if not fname.lower().endswith('.webp'):
        continue
    fpath = os.path.join(LOGOS_DIR, fname)
    fsize = os.path.getsize(fpath)
    issues = []
    w, h = 0, 0
    try:
        with Image.open(fpath) as img:
            w, h = img.size
    except Exception as e:
        issues.append(f'Cannot open: {e}')

    if w and h:
        ratio = w / h
        if ratio < 0.5 or ratio > 3.0:
            issues.append(f'Aspect {ratio:.2f} outside 0.5-3.0')
        if w < 100 or h < 100:
            issues.append(f'Res {w}x{h} below 100x100')
    if fsize < 2048:
        issues.append(f'Size {fsize}B under 2KB')

    status = 'FLAG' if issues else 'PASS'
    if issues:
        flagged += 1
    results.append((fname, w, h, fsize, status, '; '.join(issues)))

lines = [
    '# LOGO_AUDIT.md',
    f'Generated: 2026-03-20 | Logos: {len(results)} | Flagged: {flagged}',
    '',
    '| File | W | H | Size | Status | Issues |',
    '|------|---|---|------|--------|--------|',
]
for fname, w, h, fsize, status, issues in results:
    sz = f'{fsize//1024}KB' if fsize >= 1024 else f'{fsize}B'
    flag = 'FLAG' if status == 'FLAG' else 'PASS'
    lines.append(f'| {fname} | {w} | {h} | {sz} | {flag} | {issues or "-"} |')

lines += [
    '',
    '## Summary',
    f'- Total: {len(results)}',
    f'- Passed: {len(results)-flagged}',
    f'- Flagged: {flagged}',
    '',
    '## Flagged logos — re-grab targets',
    'Run regrab-logos.py to fetch replacements via Clearbit Logo API.',
]

audit_path = os.path.normpath(OUTPUT)
with open(audit_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

with open(r'D:\Work\Digital-Therapy-Solutions\assets\audit_result.txt', 'w', encoding='utf-8') as f:
    f.write(f'Audit complete. {len(results)} logos checked, {flagged} flagged.\n')
    for r in results:
        if r[4] == 'FLAG':
            f.write(f'  FLAG: {r[0]} -- {r[5]}\n')
    f.write('DONE\n')
