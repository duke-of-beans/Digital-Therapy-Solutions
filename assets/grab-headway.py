import requests
from PIL import Image
from io import BytesIO
# Google's favicon service — publicly accessible, no auth needed
url = "https://www.google.com/s2/favicons?domain=headway.co&sz=128"
r = requests.get(url, timeout=10)
print(f"Status: {r.status_code}, Size: {len(r.content)} bytes")
if r.status_code == 200:
    img = Image.open(BytesIO(r.content))
    img = img.resize((120, 120), Image.LANCZOS)
    img.save(r"D:\Work\ContentStudio\clients\digital-therapy-solutions\assets\logos\headway.webp", "WEBP", quality=90)
    print("SAVED headway.webp")
