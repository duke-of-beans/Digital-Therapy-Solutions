import sys, requests, pathlib
sys.stdout.reconfigure(encoding='utf-8')
url = "https://logo.clearbit.com/inclusivetherapists.com"
out = pathlib.Path("assets/logos/inclusive-therapists.webp")
r = requests.get(url, timeout=10)
if r.status_code == 200:
    out.write_bytes(r.content)
    print("OK:", out)
else:
    print("FAIL primary:", r.status_code, "-- trying alt domain")
    url2 = "https://logo.clearbit.com/inclusive-therapists.com"
    r2 = requests.get(url2, timeout=10)
    if r2.status_code == 200:
        out.write_bytes(r2.content)
        print("OK alt:", out)
    else:
        print("FAIL alt:", r2.status_code, "-- logging and continuing")
