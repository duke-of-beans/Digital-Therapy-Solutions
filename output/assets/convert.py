from PIL import Image
import os

assets_dir = r"D:\Work\ContentStudio\clients\digital-therapy-solutions\assets"

files = {
    "Hero - Woman on light couch with headphones.jpg": "hero.webp",
    "Video Call - Active session with earbuds.jpg": "video-call-earbuds.webp",
    "Video Call - Over the shoulder.jpg": "video-call-shoulder.webp",
}

for src_name, dst_name in files.items():
    src = os.path.join(assets_dir, src_name)
    dst = os.path.join(assets_dir, dst_name)
    
    img = Image.open(src)
    w, h = img.size
    print(f"{src_name}: {w}x{h}")
    
    # Resize: hero to 1600px wide, others to 1200px wide
    max_w = 1600 if "Hero" in src_name else 1200
    if w > max_w:
        ratio = max_w / w
        new_h = int(h * ratio)
        img = img.resize((max_w, new_h), Image.LANCZOS)
        print(f"  Resized to {max_w}x{new_h}")
    
    # Convert to WebP with quality 82 (good balance of size vs quality)
    img.save(dst, "WEBP", quality=82)
    
    src_size = os.path.getsize(src) / 1024
    dst_size = os.path.getsize(dst) / 1024
    print(f"  {src_size:.0f}KB -> {dst_size:.0f}KB ({(1 - dst_size/src_size)*100:.0f}% smaller)")
    print()

print("Done!")
