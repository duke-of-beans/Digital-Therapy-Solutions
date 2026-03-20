import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')
css = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/templates/styles.css').read_text(encoding='utf-8')
idx = css.find('platform-mini-card__price')
print(f"Line {css[:idx].count(chr(10))+1}:")
print(css[idx:idx+200])
