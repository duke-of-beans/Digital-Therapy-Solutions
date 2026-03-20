import os, re
import sys
sys.stdout.reconfigure(encoding='utf-8')

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

CORRECT_FONTS = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600&family=Instrument+Serif:ital@0;1&family=DM+Sans:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">'

CORRECT_FOOTER = '''    <footer class="site-footer">
        <div class="site-footer__inner">
            <div>
                <h3>About Digital Therapy Solutions</h3>
                <p>Independent reviews of online therapy platforms. Expert-written, regularly updated, no sponsored rankings.</p>
            </div>
            <div>
                <h3>Quick Links</h3>
                <ul><li><a href="index.html">Home</a></li><li><a href="betterhelp-review.html">Platform Reviews</a></li><li><a href="aetna.html">Insurance Guide</a></li><li><a href="about.html">About Us</a></li></ul>
            </div>
            <div>
                <h3>Resources</h3>
                <ul><li><a href="editorial-policy.html">Editorial Policy</a></li><li><a href="affiliate-disclosure.html">Affiliate Disclosure</a></li><li><a href="privacy-policy.html">Privacy Policy</a></li></ul>
            </div>
        </div>
        <div class="site-footer__crisis"><span class="crisis-alert">In crisis?</span> Call or text <a href="tel:988">988</a> &middot; Text HOME to <a href="sms:741741">741741</a> &middot; Emergency: <a href="tel:911">911</a></div>
        <div class="site-footer__bottom">&copy; 2026 Digital Therapy Solutions. All rights reserved. | <a href="privacy-policy.html">Privacy</a> | <a href="affiliate-disclosure.html">Disclosures</a></div>
    </footer>'''

# --- Fix 1: do-i-need-therapy.html ---
# Missing crisis footer - check what footer it has
fpath = os.path.join(output_dir, 'do-i-need-therapy.html')
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# Check what footer structure exists
idx = content.rfind('<footer')
print(f'do-i-need-therapy.html footer at {idx}:')
print(repr(content[idx:idx+400]))
print()

# Replace whatever footer exists with the correct one
new_content = re.sub(r'<footer.*?</footer>', CORRECT_FOOTER, content, flags=re.DOTALL)
if new_content != content:
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Fixed footer: do-i-need-therapy.html')
else:
    print('No footer found to replace in do-i-need-therapy.html')

# --- Fix 2: how-online-therapy-works.html ---
fpath2 = os.path.join(output_dir, 'how-online-therapy-works.html')
with open(fpath2, 'r', encoding='utf-8') as f:
    content2 = f.read()

# Check head
idx2 = content2.rfind('<footer')
print(f'how-online-therapy-works.html footer at {idx2}:')
print(repr(content2[idx2:idx2+200]))
print()

# Fix footer
new_content2 = re.sub(r'<footer.*?</footer>', CORRECT_FOOTER, content2, flags=re.DOTALL)

# Fix fonts - check if any font link exists
if 'fonts.googleapis.com' not in new_content2:
    # Add font links after <link rel="stylesheet"
    new_content2 = new_content2.replace(
        '<link rel="stylesheet" href="../templates/styles.css">',
        f'<link rel="preconnect" href="https://fonts.googleapis.com">\n    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n    {CORRECT_FONTS}\n    <link rel="stylesheet" href="../templates/styles.css">'
    )
    print('Added font links to how-online-therapy-works.html')

if new_content2 != content2:
    with open(fpath2, 'w', encoding='utf-8') as f:
        f.write(new_content2)
    print('Fixed: how-online-therapy-works.html')

# --- Fix 3: medicaid.html - wrong fonts ---
fpath3 = os.path.join(output_dir, 'medicaid.html')
with open(fpath3, 'r', encoding='utf-8') as f:
    content3 = f.read()

# Replace wrong font link with correct one
new_content3 = re.sub(
    r'<link[^>]+fonts\.googleapis\.com[^>]+>',
    CORRECT_FONTS,
    content3
)
# Also remove preconnect if it's to wrong fonts
if new_content3 != content3:
    with open(fpath3, 'w', encoding='utf-8') as f:
        f.write(new_content3)
    print('Fixed fonts: medicaid.html')
else:
    print('No font change needed: medicaid.html')
