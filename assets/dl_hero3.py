import urllib.request, os

assets = r'D:\Work\Digital-Therapy-Solutions\output\assets'

# Specific known good Unsplash photos for therapy/calm context
# Format: (filename, photo_id, description)
candidates = [
    # Priscilla Du Preez - two people talking warmly, soft interior
    ('try1.webp', 'photo-1573497019418-b400bb3ab074'),
    # Anthony Tran - woman looking out window, calm, warm light
    ('try2.webp', 'photo-1488717410769-e46d6b0dde52'),
    # Joice Kelly - person in calm space, warm tones
    ('try3.webp', 'photo-1490645935967-10de6ba17061'),
    # Nik Shuliahin - person sitting, calm, thoughtful
    ('try4.webp', 'photo-1541199249251-f713e6145474'),
]

base = 'https://images.unsplash.com/{id}?w=1400&h=900&fit=crop&crop=faces,top&q=80&fm=webp'

for fname, photo_id in candidates:
    url = base.format(id=photo_id)
    dest = os.path.join(assets, fname)
    print(f'Downloading {fname}...')
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
        with open(dest, 'wb') as f:
            f.write(data)
        print(f'  OK: {os.path.getsize(dest):,} bytes')
    except Exception as e:
        print(f'  FAIL: {e}')
