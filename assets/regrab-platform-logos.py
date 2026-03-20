import sys
import os
import requests
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

LOGOS_DIR = Path(r'D:\Work\Digital-Therapy-Solutions\assets\logos')
LOGOS_DIR.mkdir(parents=True, exist_ok=True)

domains = {
    "adhd-online": "adhdonline.com",
    "amwell": "amwell.com",
    "bend-health": "bendhealth.com",
    "betterhelp": "betterhelp.com",
    "brightline": "hellobrightline.com",
    "brightside": "brightside.com",
    "calmerry": "calmerry.com",
    "cerebral": "cerebral.com",
    "circle-medical": "circlemedical.com",
    "doctor-on-demand": "doctorondemand.com",
    "done-adhd": "donementalhealth.com",
    "faithful-counseling": "faithfulcounseling.com",
    "gay-therapy-center": "gaytherapycenter.com",
    "grow-therapy": "growtherapy.com",
    "headspace": "headspace.com",
    "headway": "headway.co",
    "inclusive-therapists": "inclusivetherapists.com",
    "klarity": "klarityhealth.com",
    "lunajoy": "lunajoy.com",
    "manatee-health": "manatee.co",
    "mindful-care": "mindful.care",
    "nocd": "nocdtherapy.com",
    "online-therapy": "online-therapy.com",
    "open-path": "openpathcollective.org",
    "our-relationship": "ourrelationship.com",
    "our-ritual": "ouritualtherapy.com",
    "pride-counseling": "pridecounseling.com",
    "psychology-today": "psychologytoday.com",
    "regain": "regain.us",
    "simplepractice": "simplepractice.com",
    "talkiatry": "talkiatry.com",
    "talkspace": "talkspace.com",
    "teen-counseling": "teencounseling.com",
    "therapyden": "therapyden.com",
}

results = {"pass": [], "fail": []}

for slug, domain in sorted(domains.items()):
    url = f"https://logo.clearbit.com/{domain}"
    dest = LOGOS_DIR / f"{slug}.webp"
    try:
        resp = requests.get(url, timeout=8)
        if resp.status_code == 200 and len(resp.content) > 500:
            dest.write_bytes(resp.content)
            results["pass"].append(slug)
            print(f"  PASS {slug} ({domain}) — {len(resp.content)} bytes")
        else:
            results["fail"].append(f"{slug} HTTP {resp.status_code}")
            print(f"  FAIL {slug} ({domain}) — HTTP {resp.status_code}")
    except Exception as e:
        results["fail"].append(f"{slug} {type(e).__name__}")
        print(f"  FAIL {slug} ({domain}) — {type(e).__name__}: {e}")

print(f"\nSummary: {len(results['pass'])} PASS / {len(results['fail'])} FAIL")
if results["fail"]:
    print("Failed slugs:", ", ".join(results["fail"]))
