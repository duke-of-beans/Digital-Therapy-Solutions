import sys, re
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

html = Path(r'D:\Work\Digital-Therapy-Solutions\output\anxiety.html').read_text(encoding='utf-8', errors='replace')

# Find canonical
canonical = re.findall(r'<link[^>]+canonical[^>]+>', html, re.IGNORECASE)
print('CANONICAL:', canonical[:2])

# Find meta description
meta_desc = re.findall(r'<meta[^>]+description[^>]+>', html, re.IGNORECASE)
print('META DESC:', meta_desc[:2])

# Find schema
schema = re.findall(r'"@type"\s*:\s*"([^"]+)"', html)
print('SCHEMA TYPES:', schema[:5])

# Instrument Serif
serif_refs = re.findall(r'[Ii]nstrument.{0,5}[Ss]erif', html)
print('INSTRUMENT SERIF REFS:', serif_refs[:5])

# Check CSS for font-family on stat elements
css_stat = re.findall(r'\.score-number[^{]*\{[^}]+\}', html)
print('SCORE CSS:', css_stat[:2])

# Show sitemap excerpt
sm = Path(r'D:\Work\Digital-Therapy-Solutions\output\sitemap.xml').read_text(encoding='utf-8', errors='replace')
print('\nSITEMAP (first 800 chars):')
print(sm[:800])
