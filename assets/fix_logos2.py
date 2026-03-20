import sys, pathlib, shutil
from PIL import Image
sys.stdout.reconfigure(encoding='utf-8')

base = pathlib.Path('D:/Work/Digital-Therapy-Solutions/assets/logos')
out = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/assets/logos')

# Fix Faithful-Consulting.png -> faithful-counseling.webp
src = base / 'Faithful-Consulting.png'
if src.exists():
    img = Image.open(src)
    img.save(base / 'faithful-counseling.webp', 'WEBP', quality=90)
    img.save(out / 'faithful-counseling.webp', 'WEBP', quality=90)
    print(f"Fixed: Faithful-Consulting.png -> faithful-counseling.webp {img.size}")

# Fix insurer-medicaid.webp.png -> insurer-medicaid.webp
src = base / 'insurer-medicaid.webp.png'
if src.exists():
    img = Image.open(src)
    img.save(base / 'insurer-medicaid.webp', 'WEBP', quality=90)
    img.save(out / 'insurer-medicaid.webp', 'WEBP', quality=90)
    print(f"Fixed: insurer-medicaid.webp.png -> insurer-medicaid.webp {img.size}")

# Also copy adhd-online since it's now webp
src = base / 'adhd-online.webp'
dst = out / 'adhd-online.webp'
if src.exists() and not dst.exists():
    shutil.copy2(src, dst)
    print("Copied adhd-online.webp to output")

print("Done.")
