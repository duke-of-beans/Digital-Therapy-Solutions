from PIL import Image
import os

assets = r'D:\Work\Digital-Therapy-Solutions\output\assets'
TARGET_W, TARGET_H = 1400, 900

def crop_hero(src_name, dest_name, y_pct=0.28):
    """Scale to fill width, crop vertically at y_pct from top."""
    src = os.path.join(assets, src_name)
    dest = os.path.join(assets, dest_name)
    img = Image.open(src).convert('RGB')
    w, h = img.size
    scale = TARGET_W / w
    new_h = int(h * scale)
    img_s = img.resize((TARGET_W, new_h), Image.LANCZOS)
    y_off = int(new_h * y_pct)
    if y_off + TARGET_H > new_h:
        y_off = max(0, new_h - TARGET_H)
    cropped = img_s.crop((0, y_off, TARGET_W, y_off + TARGET_H))
    cropped.save(dest, 'webp', quality=83)
    size = os.path.getsize(dest)
    print(f'{dest_name}: {cropped.size} — {size:,} bytes')

# Image 1 (back-to-window): scale to width, take mid-lower portion showing person
crop_hero('hero-emotional.webp',   'hero-emotional.webp',   y_pct=0.28)

# Image 2 (armchair): landscape, small top crop
crop_hero('hero-review.webp',      'hero-review.webp',      y_pct=0.05)

# Image 3 (floor/window smile): scale to width, take upper portion showing face
crop_hero('Hero-calm-final.webp',  'hero-calm.webp',        y_pct=0.15)

print('Done.')
