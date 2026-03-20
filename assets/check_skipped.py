import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
from bs4 import BeautifulSoup
OUTPUT_DIR = Path(r'D:\Work\Digital-Therapy-Solutions\output')
for f in sorted(OUTPUT_DIR.glob('*.html')):
    soup = BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser')
    footer = soup.find('footer', class_='site-footer')
    if not footer:
        print(f'NO FOOTER: {f.name}')
    else:
        # Check Quick Links still correct
        inner = footer.find('div', class_='site-footer__inner')
        if inner:
            for div in inner.find_all('div', recursive=False):
                h3 = div.find('h3')
                if h3 and 'Quick Links' in h3.get_text():
                    for a in div.find_all('a'):
                        href = a.get('href','')
                        if href in ('betterhelp-review.html', 'aetna.html', 'anxiety.html'):
                            print(f'STILL WRONG in {f.name}: {href}')
print('Check complete.')
