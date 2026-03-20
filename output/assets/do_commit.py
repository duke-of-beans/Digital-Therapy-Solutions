import sys
import subprocess
sys.stdout.reconfigure(encoding='utf-8')

GIT = r"d:\Program Files\Git\cmd\git.exe"
REPO = r"D:\Work\Digital-Therapy-Solutions"

def git(*args, **kwargs):
    result = subprocess.run([GIT, '-C', REPO] + list(args),
                           capture_output=True, text=True, encoding='utf-8', **kwargs)
    out = result.stdout.strip()
    err = result.stderr.strip()
    if out: print(out)
    if err: print('STDERR:', err)
    return result.returncode

print('=== git add ===')
git('add',
    'vercel.json',
    'output/404.html',
    'output/privacy-policy.html',
    'output/how-online-therapy-works.html',
    'output/betterhelp-review.html',
    'output/talkspace-review.html',
    'output/online-therapy-com-review.html',
    'output/aetna.html',
    'output/bcbs.html',
    'output/cigna.html',
    'templates/styles.css',
    'assets/patch_footer_links.py',
    'assets/regrab-platform-logos.py',
    'assets/patch_insurance_layout.py',
    'assets/patch_bcbs_cigna.py',
    'STATUS.md',
    'MORNING_BRIEFING.md',
    'commit-msg.txt',
)

# Add all the footer-patched pages (the 62 modified output/ files)
git('add', 'output/')

print('\n=== git status ===')
git('status', '--short')

print('\n=== git commit ===')
rc = git('commit', '-F', r'D:\Work\Digital-Therapy-Solutions\commit-msg.txt')
print(f'Commit exit code: {rc}')

print('\n=== git log ===')
git('log', '--oneline', '-3')

if rc == 0:
    print('\n=== git push ===')
    rc2 = git('push')
    print(f'Push exit code: {rc2}')
