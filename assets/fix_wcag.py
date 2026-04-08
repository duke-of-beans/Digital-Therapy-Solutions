import re

path = r'D:\Work\Digital-Therapy-Solutions\output\templates\styles.css'
with open(path, encoding='utf-8') as f:
    css = f.read()

# PS-DTS-WCAG-01: Strengthen visual break overlay with dark gradient + text-shadow
OLD_OVERLAY = """.visual-break__overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-xl);
}"""
NEW_OVERLAY = """.visual-break__overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-xl);
  background: linear-gradient(
    to bottom,
    rgba(0,0,0,0.15) 0%,
    rgba(0,0,0,0.35) 50%,
    rgba(0,0,0,0.55) 100%
  );
}"""
css = css.replace(OLD_OVERLAY, NEW_OVERLAY)

# PS-DTS-WCAG-01: Add text-shadow to visual break quote
OLD_QUOTE = """.visual-break__quote {
  font-family: var(--font-display);
  font-style: italic;
  font-size: clamp(1.25rem, 2.5vw, 1.75rem);
  color: white;
  line-height: 1.5;
  margin: 0 0 var(--space-sm);
}"""
NEW_QUOTE = """.visual-break__quote {
  font-family: var(--font-display);
  font-style: italic;
  font-size: clamp(1.25rem, 2.5vw, 1.75rem);
  color: white;
  line-height: 1.5;
  margin: 0 0 var(--space-sm);
  text-shadow: 0 2px 12px rgba(0,0,0,0.5), 0 1px 4px rgba(0,0,0,0.4);
}"""
css = css.replace(OLD_QUOTE, NEW_QUOTE)

with open(path, 'w', encoding='utf-8') as f:
    f.write(css)

print('WCAG overlay + text-shadow applied.')
print(f'Overlay changed: {OLD_OVERLAY in open(path, encoding="utf-8").read()} (should be False)')
