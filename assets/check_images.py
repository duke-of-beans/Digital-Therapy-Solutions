import os, re

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

# Find all hero-image src values on condition pages
conditions = [f for f in os.listdir(output_dir)
              if f.endswith('.html') and f not in [
                  'index.html','reviews.html','conditions.html','insurance.html',
                  'about.html','editorial-policy.html','affiliate-disclosure.html',
                  'privacy-policy.html','crisis-resources.html',
                  'how-online-therapy-works.html','do-i-need-therapy.html',
                  '404.html'
              ] and not f.endswith('-review.html')]

for fname in sorted(conditions):
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    heroes = re.findall(r'hero-image[^"]*"[^"]*src="([^"]+)"', content)
    if not heroes:
        heroes = re.findall(r'class="hero-image"[^>]*src="([^"]+)"', content)
    if not heroes:
        # try reversed attribute order
        heroes = re.findall(r'src="([^"]+)"[^>]*class="hero-image"', content)
    vbreaks = re.findall(r'visual-break__image[^"]*"[^"]*src="([^"]+)"', content)
    if not vbreaks:
        vbreaks = re.findall(r'class="visual-break__image"[^>]*src="([^"]+)"', content)
    print(f'{fname}:')
    print(f'  hero: {heroes}')
    print(f'  vbreak: {vbreaks}')
