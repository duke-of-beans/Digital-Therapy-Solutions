import os
d = r"D:\Work\Digital-Therapy-Solutions\output"
for f in sorted(os.listdir(d)):
    if f.endswith('.html'):
        txt = open(os.path.join(d, f), 'r', encoding='utf-8').read()
        fav = 'Y' if 'favicon.png' in txt else 'N'
        logo = 'Y' if 'logo-icon.webp' in txt else 'N'
        print(f"  {f:35s} favicon:{fav}  logo:{logo}")
