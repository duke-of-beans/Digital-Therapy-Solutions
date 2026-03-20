import os
logos_dir = r'D:\Work\Digital-Therapy-Solutions\assets\logos'
files = sorted(os.listdir(logos_dir))
lines = []
for f in files:
    size = os.path.getsize(os.path.join(logos_dir, f))
    lines.append(f"{f}: {size}")
with open(r'D:\Work\Digital-Therapy-Solutions\assets\logos_list.txt', 'w') as fh:
    fh.write('\n'.join(lines))
