import sys
import subprocess
sys.stdout.reconfigure(encoding='utf-8')

GIT = r"d:\Program Files\Git\cmd\git.exe"
REPO = r"D:\Work\Digital-Therapy-Solutions"

def git(*args):
    result = subprocess.run([GIT, '-C', REPO] + list(args),
                           capture_output=True, text=True, encoding='utf-8')
    if result.stdout: print(result.stdout)
    if result.stderr: print('STDERR:', result.stderr)
    return result.returncode

# Check if repo exists
rc = git('rev-parse', '--is-inside-work-tree')
if rc != 0:
    print('No git repo — initializing')
    git('init')
    git('add', '.')
    git('commit', '-m', 'initial commit')
else:
    print('Log:')
    git('log', '--oneline', '-5')
    print('\nStatus:')
    git('status', '--short')
