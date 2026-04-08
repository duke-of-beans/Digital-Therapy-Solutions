import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

# Condition pages missing visual break — add one before the comparison table or forks section
# These are high emotional stakes pages
targets = {
    'autism.html': {
        'image': '../assets/hero-emotional.webp',
        'alt': 'Person in a calm, comfortable environment',
        'quote': 'Finding a therapist who understands autism isn&rsquo;t just about the diagnosis label &mdash; it&rsquo;s about finding someone who understands how you actually experience the world.',
        'anchor': '<!-- COMPARISON TABLE -->',
    },
    'life-transitions.html': {
        'image': '../assets/hero-emotional.webp',
        'alt': 'Person looking out a window, contemplative',
        'quote': 'Transitions feel disorienting because they are &mdash; you&rsquo;re not broken, you&rsquo;re between two versions of yourself. Therapy helps with the in-between.',
        'anchor': '<!-- COMPARISON TABLE -->',
    },
    'mens-mental-health.html': {
        'image': '../assets/hero-focus.webp',
        'alt': 'Man sitting quietly, thoughtful',
        'quote': 'The research on why men don&rsquo;t seek help is well-established. The research on outcomes when they do is equally clear: it works. The barrier is access, not ability to benefit.',
        'anchor': '<!-- COMPARISON TABLE -->',
    },
    'womens-mental-health.html': {
        'image': '../assets/hero-emotional.webp',
        'alt': 'Woman in a calm environment, settled',
        'quote': 'Women&rsquo;s mental health needs aren&rsquo;t a specialty &mdash; they&rsquo;re the baseline. Finding a therapist who starts from that frame rather than treating it as a niche changes the whole dynamic.',
        'anchor': '<!-- COMPARISON TABLE -->',
    },
}

VISUAL_BREAK_TEMPLATE = """<!-- VISUAL BREAK -->
<div class="section-wrapper section-wrapper--visual-break">
<div class="visual-break reveal">
<img alt="{alt}" class="visual-break__image" src="{image}"/>
<div class="visual-break__overlay">
<div class="visual-break__text">
<p class="visual-break__quote">&ldquo;{quote}&rdquo;</p>
<p class="visual-break__attribution">&mdash; Digital Therapy Solutions editorial team</p>
</div>
</div>
</div>
</div>
"""

parallax_js = """
// PS-DTS-ANIM-01: Visual break parallax
(function() {
  var vb = document.querySelectorAll('.visual-break__image');
  if (!vb.length || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var ticking = false;
  window.addEventListener('scroll', function() {
    if (!ticking) {
      window.requestAnimationFrame(function() {
        vb.forEach(function(img) {
          var rect = img.closest('.visual-break').getBoundingClientRect();
          var center = rect.top + rect.height / 2 - window.innerHeight / 2;
          img.style.transform = 'translateY(' + (center * 0.18).toFixed(1) + 'px)';
        });
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });
})();"""

count = 0
for fname, cfg in targets.items():
    fpath = os.path.join(output_dir, fname)
    if not os.path.exists(fpath):
        print(f'SKIP (not found): {fname}')
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'visual-break__image' in content:
        print(f'SKIP (already has vbreak): {fname}')
        continue

    vb_html = VISUAL_BREAK_TEMPLATE.format(**cfg)

    # Insert before the anchor comment or before the comparison table section
    anchor = cfg['anchor']
    if anchor in content:
        content = content.replace(anchor, vb_html + anchor, 1)
    else:
        # Fallback: insert before the last section-wrapper--accent or forks section
        m = list(re.finditer(r'<div class="section-wrapper section-wrapper--accent">', content))
        if m:
            idx = m[0].start()
            content = content[:idx] + vb_html + content[idx:]
        else:
            print(f'WARNING: no anchor found for {fname}')
            continue

    # Also inject parallax JS if not already present
    if 'visual-break parallax' not in content:
        idx = content.rfind('</script>')
        if idx != -1:
            content = content[:idx] + parallax_js + '\n</script>' + content[idx+9:]

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f'Visual break added: {fname}')

print(f'\nDone: {count} pages updated')
