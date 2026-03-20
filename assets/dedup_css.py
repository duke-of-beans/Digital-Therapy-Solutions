import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')

path = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/templates/styles.css')
css = path.read_text(encoding='utf-8')
original_len = len(css.split('\n'))

# Rules to deduplicate: keep LAST occurrence, remove earlier ones
# Format: exact string to remove (the earlier/stale version)
removals = [
    # .hero-subhead--follow — keep line 356 (has max-width min()), remove line 371 (incomplete)
    """.hero-subhead--follow {
  font-size: clamp(1rem, 1.3vw, 1.1rem);
  margin-top: 0;
}""",
    # .condition-tile__icon duplicate — remove second occurrence (line ~2179)
    # We'll handle this by finding and removing the second one
]

# Handle condition-tile__icon — remove the duplicate
pattern = r'(\.condition-tile__icon \{ width:100%;[^\}]+\})'
matches = list(re.finditer(r'\.condition-tile__icon \{ width: 100%; display: flex; align-items: center; justify-content: center; margin-bottom: var\(--space-sm\); \}', css))
if len(matches) >= 2:
    # Remove the second occurrence
    m = matches[1]
    css = css[:m.start()] + '/* condition-tile__icon — see primary rule above */' + css[m.end():]
    print(f"Removed duplicate .condition-tile__icon at line ~{css[:m.start()].count(chr(10))+1}")

# Remove the incomplete .hero-subhead--follow at line 371
stale = """.hero-subhead--follow {
  font-size: clamp(1rem, 1.3vw, 1.1rem);
  margin-top: 0;
}"""
if stale in css:
    css = css.replace(stale, '/* .hero-subhead--follow — see primary rule with max-width */', 1)
    print("Removed stale .hero-subhead--follow (no max-width)")

# .platform-card__logo img — merge: keep both properties, remove the later partial one
# Line 460 has width/height/padding, line 2185 adds bg-secondary — merge into line 460
old_full = """.platform-card__logo img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  padding: 6px;
}"""
new_full = """.platform-card__logo img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  padding: 6px;
  background-color: var(--bg-secondary);
}"""
stale_partial = '.platform-card__logo img { object-fit: contain; background-color: var(--bg-secondary); }'
if old_full in css:
    css = css.replace(old_full, new_full, 1)
    print("Merged bg-secondary into primary .platform-card__logo img rule")
if stale_partial in css:
    css = css.replace(stale_partial, '/* .platform-card__logo img — merged above */', 1)
    print("Removed partial .platform-card__logo img duplicate")

# .insurance-tile__logo — keep the more complete one at line 2285, remove line 2182
stale_ins = '.insurance-tile__logo { object-fit: contain; background-color: var(--bg-secondary); border-radius: 6px; }'
if stale_ins in css:
    css = css.replace(stale_ins, '/* .insurance-tile__logo — see complete rule below */', 1)
    print("Removed partial .insurance-tile__logo duplicate")

path.write_text(css, encoding='utf-8')
new_len = len(css.split('\n'))
print(f"\nDone. Lines: {original_len} -> {new_len}")
