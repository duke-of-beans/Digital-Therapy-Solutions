with open(r'D:\Work\Digital-Therapy-Solutions\output\cigna.html', encoding='utf-8') as f:
    content = f.read()
idx = content.find('site-nav__links')
print(repr(content[idx:idx+400]))
