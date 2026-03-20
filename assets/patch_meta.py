import sys, os, pathlib
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

OUTPUT_DIR = pathlib.Path("output")
html_files = sorted(OUTPUT_DIR.glob("*.html"))

rows = []
for f in html_files:
    soup = BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser')
    tag = soup.find('meta', {'name': 'description'})
    if tag and tag.get('content'):
        desc = tag['content'].strip()
        n = len(desc)
        if n < 120:
            status = "SHORT"
        elif n > 160:
            status = "LONG"
        else:
            status = "PASS"
    else:
        desc = ""
        n = 0
        status = "MISSING"
    rows.append((f.name, status, n, desc))

lines = ["# META_AUDIT.md — Meta Description Audit\n",
         f"Generated: 2026-03-20 | Pages: {len(rows)}\n\n",
         "| File | Status | Chars | Description |\n",
         "|---|---|---|---|\n"]
for name, status, n, desc in rows:
    safe = desc.replace('|', '\\|')
    lines.append(f"| {name} | {status} | {n} | {safe} |\n")

summary = {"PASS": 0, "SHORT": 0, "LONG": 0, "MISSING": 0}
for _, s, _, _ in rows:
    summary[s] += 1
lines.append(f"\n## Summary\n")
for k, v in summary.items():
    lines.append(f"- {k}: {v}\n")

out = pathlib.Path("META_AUDIT.md")
out.write_text("".join(lines), encoding='utf-8')
print("META_AUDIT.md written.")
for name, status, n, desc in rows:
    print(f"  {status:7} {n:3}  {name}")
