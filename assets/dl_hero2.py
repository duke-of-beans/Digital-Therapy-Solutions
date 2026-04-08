import urllib.request, os, sys

assets = r'D:\Work\Digital-Therapy-Solutions\output\assets'

# Unsplash free images — calm, warm, settled, therapy-adjacent
# These are specific photo IDs known to be calm interior / natural light portraits
candidates = [
    # Woman by window, warm natural light, calm, thoughtful — Kelly Sikkema
    ('hero-emotional-new.webp', 'https://images.unsplash.com/photo-1531746790731-6c087fecd65a?w=1400&h=900&fit=crop&crop=faces,center&q=80&fm=webp'),
]

for fname, url in candidates:
    dest = os.path.join(assets, fname)
    print(f'Downloading {fname}...')
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
        with open(dest, 'wb') as f:
            f.write(data)
        size = os.path.getsize(dest)
        print(f'  OK: {size:,} bytes')
    except Exception as e:
        print(f'  FAIL: {e}')
