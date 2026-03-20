"""
Insurer Logo Grabber — PS-INSURANCE-01
Downloads official insurer logos as WebP, saves to assets/logos/ with insurer- prefix.
Pattern follows assets/grab-logos.py exactly.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

import requests
import re
import os
from PIL import Image
from io import BytesIO
from urllib.parse import urljoin

ASSETS_DIR = r"D:\Work\Digital-Therapy-Solutions\assets\logos"
os.makedirs(ASSETS_DIR, exist_ok=True)

INSURERS = {
    "insurer-humana":          "https://www.humana.com",
    "insurer-kaiser":          "https://healthy.kaiserpermanente.org",
    "insurer-anthem":          "https://www.anthem.com",
    "insurer-molina":          "https://www.molinahealthcare.com",
    "insurer-oscar":           "https://www.hioscar.com",
    "insurer-ambetter":        "https://www.ambetterhealth.com",
    "insurer-wellcare":        "https://www.wellcare.com",
    "insurer-tricare":         "https://www.tricare.mil",
    "insurer-chip":            "https://www.insurekidsnow.gov",
    "insurer-medicare":        "https://www.medicare.gov",
    "insurer-beacon":          "https://www.beaconhealthoptions.com",
    "insurer-magellan":        "https://www.magellanhealth.com",
    "insurer-centene":         "https://www.centene.com",
    "insurer-highmark":        "https://www.highmark.com",
    "insurer-harvard-pilgrim": "https://www.harvardpilgrim.org",
    "insurer-tufts":           "https://www.tuftshealthplan.com",
    "insurer-community-health":"https://www.chpw.org",
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

print(f"Scraping logos for {len(INSURERS)} insurers...\n")

success = 0
failed = []

for name, url in INSURERS.items():
    output_path = os.path.join(ASSETS_DIR, f"{name}.webp")

    if os.path.exists(output_path):
        print(f"  {name}: already exists, skipping")
        success += 1
        continue

    ok = False
    try:
        resp = requests.get(url, headers=HEADERS, timeout=12, allow_redirects=True)
        for icon_url in find_best_icon(resp.text, url):
            if download_icon(icon_url, output_path):
                ok = True
                break
    except Exception as e:
        print(f"  {name}: fetch error — {e}")

    if not ok:
        domain = url.replace("https://", "").replace("http://", "").split("/")[0]
        ok = google_favicon(domain, output_path)

    if ok:
        size_kb = os.path.getsize(output_path) / 1024
        print(f"  {name}: OK ({size_kb:.1f}KB)")
        success += 1
    else:
        print(f"  {name}: FAILED")
        failed.append(name)

print(f"\nDone: {success}/{len(INSURERS)} logos grabbed")
if failed:
    print(f"Failed: {', '.join(failed)}")
else:
    print("All logos grabbed successfully")
