import pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
content = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/templates/styles.css').read_text(encoding='utf-8')
idx = content.find('condition-tile__icon')
print(repr(content[idx:idx+300]))
