import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')
path = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/insurance.html')
html = path.read_text(encoding='utf-8')

old = html[html.find('<!-- LIVE: Paying Out of Pocket -->'):html.find('<!-- LIVE: Paying Out of Pocket -->')+400]
print("FOUND:")
print(old[:300])
