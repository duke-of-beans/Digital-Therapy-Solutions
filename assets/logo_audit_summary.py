import sys, pathlib
from PIL import Image
sys.stdout.reconfigure(encoding='utf-8')

LOGOS_DIR = pathlib.Path('D:/Work/Digital-Therapy-Solutions/assets/logos')
OUTPUT_DIR = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/assets/logos')

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

missing, wrong_format, not_in_output = [], [], []

for slug in EXPECTED_PLATFORMS + EXPECTED_INSURERS:
    webp = LOGOS_DIR / f'{slug}.webp'
    jpg  = LOGOS_DIR / f'{slug}.jpg'
    png  = LOGOS_DIR / f'{slug}.png'
    out  = OUTPUT_DIR / f'{slug}.webp'
    if webp.exists():
        if not out.exists(): not_in_output.append(slug)
    elif jpg.exists() or png.exists():
        wrong_format.append(slug)
    else:
        missing.append(slug)

print(f"Missing entirely ({len(missing)}): {missing if missing else 'None'}")
print(f"Wrong format ({len(wrong_format)}): {wrong_format if wrong_format else 'None'}")
print(f"Not in output ({len(not_in_output)}): {not_in_output if not_in_output else 'None'}")
print("CLEAN" if not missing and not wrong_format and not not_in_output else "ACTION NEEDED")
