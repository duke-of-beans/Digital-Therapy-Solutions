import os

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

# Hub pages already have Conditions in footer — skip them
skip = {'conditions.html', 'reviews.html', 'insurance.html'}

# The footer Quick Links block on non-hub pages has this pattern (no Conditions entry)
old = '<ul><li><a href="index.html">Home</a></li><li><a href="reviews.html">Platform Reviews</a></li><li><a href="insurance.html">Insurance Guide</a></li><li><a href="about.html">About Us</a></li></ul>'
new = '<ul><li><a href="index.html">Home</a></li><li><a href="reviews.html">Platform Reviews</a></li><li><a href="conditions.html">Conditions</a></li><li><a href="insurance.html">Insurance Guide</a></li><li><a href="about.html">About Us</a></li></ul>'

count = 0
skipped = 0
for fname in os.listdir(output_dir):
    if not fname.endswith('.html'):
        continue
    if fname in skip:
        skipped += 1
        continue
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f'Footer Conditions link added to {count} files ({skipped} hub pages skipped)')
