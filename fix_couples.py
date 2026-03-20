import re

fpath = r'D:\Work\Digital-Therapy-Solutions\output\couples.html'
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the context around href="/"
idx = content.find('href="/"')
print('Context:', repr(content[max(0,idx-50):idx+80]))

# Fix: replace href="/" with href="index.html" - but only if it's not part of site-nav brand
# The brand link would be: href="/" class="site-nav__brand" - already handled
# Any remaining href="/" is a dead absolute path
fixed = content.replace('href="/"', 'href="index.html"')
if fixed != content:
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(fixed)
    print('Fixed href="/" -> href="index.html"')
else:
    print('No change')
