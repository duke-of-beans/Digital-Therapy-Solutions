import pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
css = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/templates/styles.css').read_text(encoding='utf-8')
idx = css.find('hero-subhead')
print(css[idx:idx+500])
