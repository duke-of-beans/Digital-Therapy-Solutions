import os
assets = r'D:\Work\Digital-Therapy-Solutions\output\assets'
for f in ['hero-emotional.webp', 'hero-review.webp', 'hero-calm.webp']:
    path = os.path.join(assets, f)
    if os.path.exists(path):
        print(f'{f}: {os.path.getsize(path):,} bytes')
    else:
        print(f'{f}: NOT FOUND')
