import requests
from PIL import Image
from io import BytesIO
import os
for name, domain in [("klarity", "klaritymind.com"), ("lunajoy", "lunajoy.us")]:
    out = rf"D:\Work\ContentStudio\clients\digital-therapy-solutions\assets\logos\{name}.webp"
    for d in [domain, f"www.{domain}"]:
        url = f"https://www.google.com/s2/favicons?domain={d}&sz=128"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200 and len(r.content) > 100:
                img = Image.open(BytesIO(r.content))
                img = img.resize((120, 120), Image.LANCZOS)
                img.save(out, "WEBP", quality=90)
                print(f"{name}: OK from {d} ({os.path.getsize(out)/1024:.1f}KB)")
                break
        except Exception as e:
            print(f"{name}: {d} failed - {e}")
