import pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
for p in pathlib.Path('D:/Work/Digital-Therapy-Solutions').rglob('styles.css'):
    size = p.stat().st_size
    print(f"{p} ({size} bytes)")
