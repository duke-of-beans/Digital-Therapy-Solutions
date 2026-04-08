import urllib.request, os

assets = r'D:\Work\Digital-Therapy-Solutions\output\assets'

# Targeted specific known photos — calm, warm, people, settled
candidates = [
    # Priscilla Du Preez — woman relaxing on sofa, warm light, soft background, genuinely calm
    ('cand_a.webp', 'photo-1544005313-94ddf0286df2?w=1400&h=900&fit=crop&crop=faces,top&q=80&fm=webp'),
    # Brooke Cagle — woman on couch with mug, warm sunlit interior, peaceful
    ('cand_b.webp', 'photo-1554151228-14d9def656e4?w=1400&h=900&fit=crop&crop=faces,top&q=80&fm=webp'),
    # Anthony Tran — woman looking out window, natural warm light, introspective
    ('cand_c.webp', 'photo-1499728603263-13726abce5fd?w=1400&h=900&fit=crop&crop=top&q=80&fm=webp'),
    # Priscilla Du Preez — person sitting, calm, warm indoor tones
    ('cand_d.webp', 'photo-1488521787991-ed7bbaae773c?w=1400&h=900&fit=crop&crop=faces,top&q=80&fm=webp'),
]

base = 'https://images.unsplash.com/{id}'
for fname, photo_id in candidates:
    url = base.format(id=photo_id)
    dest = os.path.join(assets, fname)
    print(f'Fetching {fname}...')
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = resp.read()
        with open(dest, 'wb') as f:
            f.write(data)
        print(f'  {os.path.getsize(dest):,} bytes')
    except Exception as e:
        print(f'  FAIL: {e}')
