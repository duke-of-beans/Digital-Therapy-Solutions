import os

assets = r'D:\Work\Digital-Therapy-Solutions\output\assets'
to_delete = [
    'cand_a.webp', 'cand_b.webp', 'cand_c.webp', 'cand_d.webp',
    'try1.webp', 'try3.webp', 'try4.webp',
    'hero-emotional-new.webp', 'Hero-calm-final.webp'
]
for f in to_delete:
    path = os.path.join(assets, f)
    if os.path.exists(path):
        os.remove(path)
        print(f'Deleted: {f}')
    else:
        print(f'Not found: {f}')
