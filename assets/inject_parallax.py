import os, re

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

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
for fname in os.listdir(output_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Only pages with visual break AND the standard closing script block
    if 'visual-break__image' not in content:
        continue
    # Insert before </script> at the bottom (the last </script> before </body>)
    if parallax_js.strip()[:30] in content:
        continue  # already injected
    # Find the last </script> before </body>
    idx = content.rfind('</script>')
    if idx == -1:
        continue
    content = content[:idx] + parallax_js + '\n</script>' + content[idx+9:]
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f'  Parallax added: {fname}')

print(f'\nTotal: {count} pages updated')
