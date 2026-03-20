import os, re

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

# All 13 original pages (new 8 pages already have correct footer/brand)
old_pages = ['adhd.html','aetna.html','affordable.html','anxiety.html','bcbs.html',
             'betterhelp-review.html','cigna.html','couples.html','depression.html',
             'medicaid.html','online-therapy-com-review.html','talkspace-review.html',
             'unitedhealthcare.html']

nav_brand_new = '''<a href="index.html" class="site-nav__brand">
                <img src="../assets/branding/logo-icon.webp" alt="" class="site-nav__brand-icon">
                Digital Therapy Solutions
            </a>'''

footer_new = '''<footer class="site-footer">
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

updated = []

for fname in old_pages:
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Fix nav brand — replace any <a href="/" class="site-nav__brand">...</a> with logo version
    # Handle both: simple text brand and already-logo brand
    content = re.sub(
        r'<a\s+href="[^"]*"\s+class="site-nav__brand"[^>]*>.*?</a>',
        nav_brand_new,
        content,
        flags=re.DOTALL
    )

    # 2. Replace entire <footer ... </footer> block
    content = re.sub(
        r'<footer class="site-footer">.*?</footer>',
        footer_new,
        content,
        flags=re.DOTALL
    )

    # 3. Fix absolute footer/nav links that might remain (e.g. href="/conditions")
    content = content.replace('href="/conditions"', 'href="anxiety.html"')
    content = content.replace('href="/insurance"', 'href="aetna.html"')
    content = content.replace('href="/reviews"', 'href="betterhelp-review.html"')
    content = content.replace('href="/about"', 'href="about.html"')
    content = content.replace('href="/privacy"', 'href="privacy-policy.html"')
    content = content.replace('href="/terms"', 'href="privacy-policy.html"')
    content = content.replace('href="/editorial-policy"', 'href="editorial-policy.html"')
    content = content.replace('href="/affiliate-disclosure"', 'href="affiliate-disclosure.html"')

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated.append(fname)

print(f'Updated {len(updated)} files:')
for f in updated:
    print(f'  {f}')
if len(updated) < len(old_pages):
    missed = [p for p in old_pages if p not in updated]
    print(f'No change needed: {missed}')
