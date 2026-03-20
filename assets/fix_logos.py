import sys, pathlib
from PIL import Image
sys.stdout.reconfigure(encoding='utf-8')

base = pathlib.Path('D:/Work/Digital-Therapy-Solutions/assets/logos')
out = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/assets/logos')

# Convert adhd-online.png to webp
png = base / 'adhd-online.png'
webp = base / 'adhd-online.webp'
if png.exists():
    img = Image.open(png)
    img.save(webp, 'WEBP', quality=90)
    print(f"Converted: adhd-online.png -> adhd-online.webp ({img.size})")
    # Copy to output
    img.save(out / 'adhd-online.webp', 'WEBP', quality=90)
    print(f"Copied to output/assets/logos/adhd-online.webp")

# Copy the 3 insurer webps that exist but aren't in output
for slug in ['insurer-bcbs', 'insurer-aetna', 'insurer-cigna', 'insurer-unitedhealthcare']:
    src = base / f'{slug}.webp'
    dst = out / f'{slug}.webp'
    if src.exists():
        img = Image.open(src)
        # Resize large wordmarks to max 400px wide for card use
        if img.width > 400:
            ratio = 400 / img.width
            new_size = (400, int(img.height * ratio))
            img = img.resize(new_size, Image.LANCZOS)
            print(f"Resized {slug}: -> {img.size}")
        img.save(dst, 'WEBP', quality=90)
        img.save(src, 'WEBP', quality=90)
        print(f"Copied {slug}.webp to output")
    else:
        print(f"MISSING: {slug}.webp not found in assets/logos/")

print("Done.")
