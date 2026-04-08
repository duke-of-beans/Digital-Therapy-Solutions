import urllib.request, os

# Anthony Tran - woman relaxed on couch, warm natural window light, genuine, calm
url = 'https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=1400&h=900&fit=crop&crop=top&q=80&fm=webp'
dest = r'D:\Work\Digital-Therapy-Solutions\output\assets\hero-emotional-new.webp'
urllib.request.urlretrieve(url, dest)
size = os.path.getsize(dest)
print(f'Downloaded {size:,} bytes -> {dest}')
