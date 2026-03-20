import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')
css = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/templates/styles.css').read_text(encoding='utf-8')
# Find reveal CSS rules
matches = re.findall(r'\.reveal[^\{]*\{[^\}]+\}', css)
for m in matches[:10]:
    print(m[:150])
    print('---')
