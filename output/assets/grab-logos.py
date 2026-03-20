"""
Logo Scraper v2 — ALL platforms referenced in the DTS site architecture.
Downloads apple-touch-icon or best available, converts to 120x120 WebP.
Falls back to Google favicon cache for stubborn CDNs.
"""
import requests
import re
import os
from PIL import Image
from io import BytesIO
from urllib.parse import urljoin

ASSETS_DIR = r"D:\Work\ContentStudio\clients\digital-therapy-solutions\assets\logos"
os.makedirs(ASSETS_DIR, exist_ok=True)

# Every platform referenced in SITE_ARCHITECTURE_SPEC.md + competitive research
PLATFORMS = {
    # Primary affiliate programs
    "online-therapy": "https://www.online-therapy.com",
    "betterhelp": "https://www.betterhelp.com",
    "talkspace": "https://www.talkspace.com",
    "calmerry": "https://www.calmerry.com",
    # Major platforms (appear in comparison/review pages)
    "headway": "https://headway.co",
    "brightside": "https://www.brightside.com",
    "grow-therapy": "https://www.growtherapy.com",
    "headspace": "https://www.headspace.com",
    "open-path": "https://www.openpathcollective.org",
    # Specialty platforms
    "nocd": "https://www.treatmyocd.com",
    "talkiatry": "https://www.talkiatry.com",
    "klarity": "https://www.klaritymind.com",
    "adhd-online": "https://adhdonline.com",
    "circle-medical": "https://www.circlemedical.com",
    "cerebral": "https://cerebral.com",
    "doctor-on-demand": "https://doctorondemand.com",
    "amwell": "https://www.amwell.com",
    "mindful-care": "https://www.mindful.care",
    "done-adhd": "https://www.donefirst.com",
    # BetterHelp sub-brands
    "regain": "https://www.regain.us",
    "teen-counseling": "https://www.teencounseling.com",
    "faithful-counseling": "https://www.faithfulcounseling.com",
    "pride-counseling": "https://www.pridecounseling.com",
    # Couples/specialty
    "our-ritual": "https://www.ourritual.com",
    "our-relationship": "https://www.ourrelationship.com",
    # Kids/teens
    "bend-health": "https://www.bendhealth.com",
    "manatee-health": "https://www.manateehealth.com",
    "brightline": "https://www.hellobrightline.com",
    # Niche/emerging
    "lunajoy": "https://www.lunajoy.us",
    "inclusive-therapists": "https://www.inclusivetherapists.com",
    "gay-therapy-center": "https://www.gaytherapycenter.com",
    # Directories (referenced in spec)
    "psychology-today": "https://www.psychologytoday.com",
    "therapyden": "https://www.therapyden.com",
    "simplepractice": "https://www.simplepractice.com",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def find_best_icon(html, base_url):
    candidates = []
    for pattern in [
        r'<link[^>]*rel=["\']apple-touch-icon["\'][^>]*href=["\']([^"\']+)["\']',
        r'<link[^>]*href=["\']([^"\']+)["\'][^>]*rel=["\']apple-touch-icon["\']',
        r'<meta[^>]*property=["\']og:image["\'][^>]*content=["\']([^"\']+)["\']',
        r'<meta[^>]*content=["\']([^"\']+)["\'][^>]*property=["\']og:image["\']',
        r'<link[^>]*rel=["\'](?:shortcut )?icon["\'][^>]*href=["\']([^"\']+)["\']',
        r'<link[^>]*href=["\']([^"\']+)["\'][^>]*rel=["\'](?:shortcut )?icon["\']',
    ]:
        for m in re.findall(pattern, html, re.I):
            candidates.append(urljoin(base_url, m))
    candidates.append(urljoin(base_url, "/favicon.ico"))
    return candidates

def download_icon(url, output_path, size=120):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10, allow_redirects=True)
        resp.raise_for_status()
        img = Image.open(BytesIO(resp.content))
        img = img.convert('RGBA') if img.mode in ('RGBA', 'LA', 'P') else img.convert('RGB')
        img = img.resize((size, size), Image.LANCZOS)
        img.save(output_path, 'WEBP', quality=90)
        return True
    except:
        return False

def google_favicon(domain, output_path, size=120):
    try:
        url = f"https://www.google.com/s2/favicons?domain={domain}&sz=128"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            img = Image.open(BytesIO(resp.content))
            img = img.resize((size, size), Image.LANCZOS)
            img.save(output_path, 'WEBP', quality=90)
            return True
    except:
        pass
    return False

print(f"Scraping logos for {len(PLATFORMS)} platforms...\n")

success = 0
failed = []

for name, url in PLATFORMS.items():
    output_path = os.path.join(ASSETS_DIR, f"{name}.webp")
    
    # Skip if already exists
    if os.path.exists(output_path):
        print(f"  {name}: already exists, skipping")
        success += 1
        continue
    
    ok = False
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10, allow_redirects=True)
        for icon_url in find_best_icon(resp.text, url):
            if download_icon(icon_url, output_path):
                ok = True
                break
    except:
        pass
    
    if not ok:
        # Fallback to Google favicon cache
        domain = url.replace("https://", "").replace("http://", "").split("/")[0]
        ok = google_favicon(domain, output_path)
    
    if ok:
        size_kb = os.path.getsize(output_path) / 1024
        print(f"  {name}: OK ({size_kb:.1f}KB)")
        success += 1
    else:
        print(f"  {name}: FAILED")
        failed.append(name)

print(f"\nDone: {success}/{len(PLATFORMS)} logos scraped")
if failed:
    print(f"Failed: {', '.join(failed)}")
print(f"\nTotal platforms: {len(PLATFORMS)}")
print(f"Trust badge should say: '{len(PLATFORMS)}+ Platforms Reviewed'")
