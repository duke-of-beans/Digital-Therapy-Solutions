import os, re

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

old_pages = ['adhd.html','aetna.html','affordable.html','anxiety.html','bcbs.html',
             'betterhelp-review.html','cigna.html','couples.html','depression.html',
             'medicaid.html','online-therapy-com-review.html','talkspace-review.html',
             'unitedhealthcare.html']

new_nav_links = """                <li><a href="index.html">Home</a></li>
                <li><a href="anxiety.html">Conditions</a></li>
                <li><a href="betterhelp-review.html">Reviews</a></li>
                <li><a href="aetna.html">Insurance</a></li>
                <li><a href="about.html">About</a></li>"""

updated = []
skipped = []

for fname in old_pages:
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match the ul.site-nav__links block and replace its contents
    old_nav_pattern = r'(<ul class="site-nav__links">)(.*?)(</ul>)'
    
    new_content = re.sub(
        old_nav_pattern,
        '<ul class="site-nav__links">\n' + new_nav_links + '\n            </ul>',
        content,
        flags=re.DOTALL
    )
    
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated.append(fname)
    else:
        skipped.append(fname)

print('Updated:', len(updated), updated)
print('Skipped (no change):', len(skipped), skipped)
