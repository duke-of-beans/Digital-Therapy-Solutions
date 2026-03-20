import sys, os, urllib.request, ssl
sys.stdout.reconfigure(encoding='utf-8')

LOGOS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logos')
RESULT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'regrab_result.txt')

# Map: filename -> clearbit domain
TARGETS = {
    'adhd-online.webp':          'adhdonline.com',
    'bend-health.webp':          'bendhealth.com',
    'betterhelp.webp':           'betterhelp.com',
    'brightside.webp':           'brightside.com',
    'doctor-on-demand.webp':     'doctorondemand.com',
    'done-adhd.webp':            'donefirst.com',
    'faithful-counseling.webp':  'faithfulcounseling.com',
    'grow-therapy.webp':         'growtherapy.com',
    'headway.webp':              'headway.co',
    'insurer-anthem.webp':       'anthem.com',
    'insurer-chip.webp':         'insurekidsnow.gov',
    'insurer-humana.webp':       'humana.com',
    'insurer-magellan.webp':     'magellanhealth.com',
    'insurer-medicare.webp':     'medicare.gov',
    'insurer-wellcare.webp':     'wellcare.com',
    'mindful-care.webp':         'mindful.care',
    'nocd.webp':                 'treatmyocd.com',
    'open-path.webp':            'openpathcollective.org',
    'our-ritual.webp':           'ourritual.com',
    'pride-counseling.webp':     'pridecounseling.com',
    'psychology-today.webp':     'psychologytoday.com',
    'simplepractice.webp':       'simplepractice.com',
    'talkspace.webp':            'talkspace.com',
}

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

results = []
for fname, domain in TARGETS.items():
    url = f'https://logo.clearbit.com/{domain}?size=200&format=png'
    dest = os.path.join(LOGOS_DIR, fname)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = resp.read()
        if len(data) > 500:
            with open(dest, 'wb') as f:
                f.write(data)
            results.append(f'OK  {fname} ({len(data)//1024}KB from {domain})')
        else:
            results.append(f'SKIP {fname} -- response too small ({len(data)}B)')
    except Exception as e:
        results.append(f'FAIL {fname} -- {e}')

with open(RESULT_FILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(results) + '\nDONE\n')
