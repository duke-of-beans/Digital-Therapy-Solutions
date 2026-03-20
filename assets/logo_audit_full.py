import sys, os, pathlib
from PIL import Image
sys.stdout.reconfigure(encoding='utf-8')

LOGOS_DIR = pathlib.Path('D:/Work/Digital-Therapy-Solutions/assets/logos')
OUTPUT_DIR = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/assets/logos')

# Expected full set — platforms + insurers
EXPECTED_PLATFORMS = [
    'adhd-online','amwell','bend-health','betterhelp','brightline','brightside',
    'calmerry','cerebral','circle-medical','doctor-on-demand','done-adhd',
    'faithful-counseling','gay-therapy-center','grow-therapy','headspace','headway',
    'inclusive-therapists','klarity','lunajoy','manatee-health','mindful-care',
    'nocd','online-therapy','open-path','our-relationship','our-ritual',
    'pride-counseling','psychology-today','regain','simplepractice','talkiatry',
    'talkspace','teen-counseling','therapyden'
]
EXPECTED_INSURERS = [
    'insurer-aetna','insurer-bcbs','insurer-cigna','insurer-unitedhealthcare',
    'insurer-medicaid','insurer-humana','insurer-kaiser','insurer-anthem',
    'insurer-molina','insurer-oscar','insurer-ambetter','insurer-wellcare',
    'insurer-tricare','insurer-chip','insurer-medicare','insurer-beacon',
    'insurer-magellan','insurer-centene','insurer-highmark','insurer-harvard-pilgrim',
    'insurer-tufts','insurer-community-health'
]
ALL_EXPECTED = EXPECTED_PLATFORMS + EXPECTED_INSURERS

print("=" * 60)
print("LOGO AUDIT")
print("=" * 60)

missing = []
wrong_format = []
in_output = []
not_in_output = []

for slug in ALL_EXPECTED:
    webp = LOGOS_DIR / f'{slug}.webp'
    jpg  = LOGOS_DIR / f'{slug}.jpg'
    png  = LOGOS_DIR / f'{slug}.png'
    out  = OUTPUT_DIR / f'{slug}.webp'

    if webp.exists():
        try:
            img = Image.open(webp)
            w, h = img.size
            size = webp.stat().st_size
            status = 'OK' if size > 1000 else 'TINY'
            ratio = f'{w}x{h}'
        except:
            status = 'CORRUPT'
            ratio = '?'
        in_out = 'in-output' if out.exists() else 'MISSING-from-output'
        print(f"[{status:7}] {slug}.webp ({ratio}, {size//1024}KB) | {in_out}")
        if not out.exists():
            not_in_output.append(slug)
    elif jpg.exists():
        size = jpg.stat().st_size
        print(f"[NEEDS-CONV] {slug}.jpg ({size//1024}KB) — needs webp conversion")
        wrong_format.append(slug)
    elif png.exists():
        size = png.stat().st_size
        print(f"[NEEDS-CONV] {slug}.png ({size//1024}KB) — needs webp conversion")
        wrong_format.append(slug)
    else:
        print(f"[MISSING   ] {slug} — not in assets/logos/")
        missing.append(slug)

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Missing entirely: {len(missing)}")
for m in missing: print(f"  - {m}")
print(f"Wrong format (needs conversion): {len(wrong_format)}")
for m in wrong_format: print(f"  - {m}")
print(f"Not copied to output/assets/logos/: {len(not_in_output)}")
for m in not_in_output: print(f"  - {m}")
