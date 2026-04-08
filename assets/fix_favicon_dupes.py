import os, re

output_dir = r'D:\Work\Digital-Therapy-Solutions\output'

# Detect and remove duplicate favicon/apple-touch-icon link tags in <head>
# Pattern: identical <link rel="icon"> or <link rel="apple-touch-icon"> appearing twice

favicon_pat = re.compile(r'(<link href="../assets/branding/favicon\.png" rel="icon" type="image/png"/>)\s*\n(\s*<link href="../assets/branding/apple-touch-icon\.png" rel="apple-touch-icon"/>)\s*\n(.*?)(\1\s*\n\s*\2)', re.DOTALL)

count_files = 0
count_dupes = 0

for fname in os.listdir(output_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(output_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Count occurrences of the favicon line
    favicon_count = content.count('<link href="../assets/branding/favicon.png" rel="icon" type="image/png"/>')
    touch_count = content.count('<link href="../assets/branding/apple-touch-icon.png" rel="apple-touch-icon"/>')

    if favicon_count > 1 or touch_count > 1:
        # Remove the duplicate pair — keep first occurrence, remove second
        new_content = content
        if favicon_count > 1:
            # Remove the second occurrence
            idx = new_content.find('<link href="../assets/branding/favicon.png" rel="icon" type="image/png"/>')
            idx2 = new_content.find('<link href="../assets/branding/favicon.png" rel="icon" type="image/png"/>', idx + 1)
            if idx2 != -1:
                new_content = new_content[:idx2] + new_content[idx2 + len('<link href="../assets/branding/favicon.png" rel="icon" type="image/png"/>'):]
        if touch_count > 1:
            idx = new_content.find('<link href="../assets/branding/apple-touch-icon.png" rel="apple-touch-icon"/>')
            idx2 = new_content.find('<link href="../assets/branding/apple-touch-icon.png" rel="apple-touch-icon"/>', idx + 1)
            if idx2 != -1:
                new_content = new_content[:idx2] + new_content[idx2 + len('<link href="../assets/branding/apple-touch-icon.png" rel="apple-touch-icon"/>'):]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count_files += 1
        count_dupes += (favicon_count - 1) + (touch_count - 1)
        print(f'  Fixed: {fname} (favicon x{favicon_count}, touch x{touch_count})')

print(f'\nDuplicate favicon tags removed: {count_dupes} across {count_files} files')
