from PIL import Image
import os

logos = {
    r"D:\Downloads\Klarity Logo.png": r"D:\Work\ContentStudio\clients\digital-therapy-solutions\assets\logos\klarity.webp",
    r"D:\Downloads\LunaJoy Logo.png": r"D:\Work\ContentStudio\clients\digital-therapy-solutions\assets\logos\lunajoy.webp",
}

for src, dst in logos.items():
    img = Image.open(src)
    print(f"{os.path.basename(src)}: {img.size[0]}x{img.size[1]}")
    img = img.resize((120, 120), Image.LANCZOS)
    img.save(dst, "WEBP", quality=90)
    print(f"  -> {os.path.basename(dst)} ({os.path.getsize(dst)/1024:.1f}KB)")

print("\nDone! 34/34 logos complete.")
