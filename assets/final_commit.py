import sys
import subprocess
sys.stdout.reconfigure(encoding='utf-8')

GIT = r"d:\Program Files\Git\cmd\git.exe"
REPO = r"D:\Work\Digital-Therapy-Solutions"

def git(*args):
    result = subprocess.run([GIT, '-C', REPO] + list(args),
                           capture_output=True, text=True, encoding='utf-8')
    if result.stdout.strip(): print(result.stdout.strip())
    if result.stderr.strip(): print('STDERR:', result.stderr.strip())
    return result.returncode

git('add', 'STATUS.md')
git('commit', '-m', 'chore: add PS-DESIGN-QA-02 commit hash to STATUS.md')
git('push')
git('log', '--oneline', '-3')
