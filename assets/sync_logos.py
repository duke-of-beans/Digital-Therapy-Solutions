from PIL import Image
import pathlib, sys, shutil
sys.stdout.reconfigure(encoding='utf-8')

slugs = ['insurer-aetna','insurer-bcbs','insurer-cigna','insurer-unitedhealthcare']
base = pathlib.Path('D:/Work/Digital-Therapy-Solutions/assets/logos')
out  = pathlib.Path('D:/Work/Digital-Therapy-Solutions/output/assets/logos')

for s in slugs:
    src = base / f'{s}.webp'
    dst = out / f'{s}.webp'
    si = Image.open(src).size if src.exists() else None
    di = Image.open(dst).size if dst.exists() else None
    print(f'{s}:  src={si}  output={di}')
    # Always copy src -> output fresh (src is the canonical version)
    if src.exists():
        shutil.copy2(src, dst)
        print(f'  -> copied to output')
