import os, re

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'
pages = ['cigna.html', 'medicaid.html']

new_nav_ul = '''<ul class="site-nav__links">
                <li><a href="index.html">Home</a></li>
                <li><a href="anxiety.html">Conditions</a></li>
                <li><a href="betterhelp-review.html">Reviews</a></li>
                <li><a href="aetna.html">Insurance</a></li>
                <li><a href="about.html">About</a></li>
            </ul>'''

updated = []
for fname in pages:
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # These pages have: site-nav__links">\n ... links ... \n</div>
    # Replace the entire nav links block
    new_content = re.sub(
        r'site-nav__links">(.*?)</div>',
        'site-nav__links">\n                <li><a href="index.html">Home</a></li>\n                <li><a href="anxiety.html">Conditions</a></li>\n                <li><a href="betterhelp-review.html">Reviews</a></li>\n                <li><a href="aetna.html">Insurance</a></li>\n                <li><a href="about.html">About</a></li>\n            </ul>',
        content,
        flags=re.DOTALL
    )
    
    # Also fix the tag from div to ul if needed
    # Check if we still have a closing </div> that should be </ul>
    
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated.append(fname)
        print(f'Updated: {fname}')
    else:
        print(f'No change: {fname}')
        # Try alternate pattern
        print('Trying alternate...')
        new_content2 = content.replace(
            'site-nav__links">',
            'site-nav__links">'
        )
        print('Content around nav:')
        idx = content.find('site-nav__links')
        print(repr(content[idx:idx+500]))
