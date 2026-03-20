import sys, re, pathlib
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')

path = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/insurance.html')
html = path.read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')

fixed = 0
for card in soup.select('.hub-card'):
    # Find the colored wrapper div with inline style containing background color
    wrapper = card.find('div', style=re.compile(r'background:#'))
    if not wrapper:
        continue
    img = wrapper.find('img')
    if not img:
        continue
    # Remove inline styles from img, replace with clean class-based approach
    img['style'] = 'width:40px;height:40px;object-fit:contain;display:block;margin-bottom:8px;'
    img['class'] = ['insurance-hub__logo']
    # Replace the colored wrapper div with just the img
    wrapper.replace_with(img)
    fixed += 1

path.write_text(str(soup), encoding='utf-8')
print(f"Fixed {fixed} hub cards")
