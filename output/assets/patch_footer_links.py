import sys
import os
from pathlib import Path
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

OUTPUT_DIR = Path(r"D:\Work\Digital-Therapy-Solutions\output")
html_files = sorted(OUTPUT_DIR.glob("*.html"))

patched = 0
skipped = 0
resources_patched = 0

for filepath in html_files:
    original = filepath.read_text(encoding='utf-8')
    soup = BeautifulSoup(original, 'html.parser')

    footer = soup.find('footer', class_='site-footer')
    if not footer:
        print(f"  SKIP (no footer): {filepath.name}")
        skipped += 1
        continue

    changed = False

    # --- Issue 2: Fix Quick Links section ---
    # Find all <ul> in footer — Quick Links is the second <div> child
    footer_divs = footer.find('div', class_='site-footer__inner')
    if footer_divs:
        divs = footer_divs.find_all('div', recursive=False)
        # Quick Links is the div with an <h3> containing "Quick Links"
        for div in divs:
            h3 = div.find('h3')
            if h3 and 'Quick Links' in h3.get_text():
                ul = div.find('ul')
                if ul:
                    for a in ul.find_all('a'):
                        href = a.get('href', '')
                        # betterhelp-review.html -> reviews.html
                        if href == 'betterhelp-review.html':
                            a['href'] = 'reviews.html'
                            if a.get_text(strip=True) not in ('Platform Reviews',):
                                pass  # keep existing text
                            changed = True
                            print(f"  FIX Quick Links betterhelp-review -> reviews.html: {filepath.name}")
                        # aetna.html -> insurance.html
                        if href == 'aetna.html':
                            a['href'] = 'insurance.html'
                            changed = True
                            print(f"  FIX Quick Links aetna -> insurance.html: {filepath.name}")
                        # anxiety.html -> conditions.html (if in footer only)
                        if href == 'anxiety.html':
                            a['href'] = 'conditions.html'
                            changed = True
                            print(f"  FIX Quick Links anxiety -> conditions.html: {filepath.name}")

            # --- Issue 5: Ensure Resources section has all 3 links ---
            if h3 and 'Resources' in h3.get_text():
                ul = div.find('ul')
                if not ul:
                    ul = soup.new_tag('ul')
                    div.append(ul)
                    changed = True

                existing_hrefs = {a.get('href', '') for a in ul.find_all('a')}

                required = [
                    ('editorial-policy.html', 'Editorial Policy'),
                    ('affiliate-disclosure.html', 'Affiliate Disclosure'),
                    ('privacy-policy.html', 'Privacy Policy'),
                ]
                for href, label in required:
                    if href not in existing_hrefs:
                        li = soup.new_tag('li')
                        a = soup.new_tag('a', href=href)
                        a.string = label
                        li.append(a)
                        ul.append(li)
                        changed = True
                        resources_patched += 1
                        print(f"  ADD Resources link {href}: {filepath.name}")

    if changed:
        filepath.write_text(str(soup), encoding='utf-8')
        patched += 1
    else:
        skipped += 1

print(f"\nDone. Patched: {patched} files | Resources links added: {resources_patched} | Skipped: {skipped}")
