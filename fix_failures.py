import os, re
import sys
sys.stdout.reconfigure(encoding='utf-8')

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

# Fix 1: do-i-need-therapy.html and how-online-therapy-works.html missing crisis-alert class
# The footer crisis line needs: <span class="crisis-alert">In crisis?</span>
# Check what they have

for fname in ['do-i-need-therapy.html', 'how-online-therapy-works.html']:
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the footer crisis section
    idx = content.find('site-footer__crisis')
    if idx >= 0:
        print(f'{fname} footer crisis section:')
        print(repr(content[idx:idx+200]))
    else:
        print(f'{fname}: NO site-footer__crisis div found!')
    print()

# Fix 2: how-online-therapy-works.html missing Fraunces font
fname2 = 'how-online-therapy-works.html'
fpath2 = os.path.join(output_dir, fname2)
with open(fpath2, 'r', encoding='utf-8') as f:
    content2 = f.read()
idx2 = content2.find('fonts.googleapis')
print(f'{fname2} font link:')
print(repr(content2[idx2:idx2+200]) if idx2 >= 0 else 'NO FONT LINK FOUND')
print()

# Fix 3: medicaid.html missing Fraunces font
fname3 = 'medicaid.html'
fpath3 = os.path.join(output_dir, fname3)
with open(fpath3, 'r', encoding='utf-8') as f:
    content3 = f.read()
idx3 = content3.find('fonts.googleapis')
print(f'{fname3} font link:')
print(repr(content3[idx3:idx3+200]) if idx3 >= 0 else 'NO FONT LINK FOUND')
