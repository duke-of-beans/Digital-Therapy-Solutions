import os
out = r'D:\Work\Digital-Therapy-Solutions\output'
counts = {}
for f in os.listdir(out):
    if not f.endswith('.html'): continue
    c = open(os.path.join(out,f), encoding='utf-8').read()
    for img in ['hero-emotional','hero-focus','hero-practical','hero-couples','hero-review']:
        if img in c:
            counts[img] = counts.get(img, 0) + 1

print('Image usage:')
for k,v in sorted(counts.items(), key=lambda x: -x[1]):
    print(f'  {k}.webp: {v} pages')

print()
assets = r'D:\Work\Digital-Therapy-Solutions\output\assets'
webps = [f for f in os.listdir(assets) if f.endswith('.webp') and 'hero' in f.lower()]
print('Available hero webp assets:')
for w in sorted(webps):
    print(f'  {w}')
