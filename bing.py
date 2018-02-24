#!/usr/bin/env python 

import requests
import time
import os
from subprocess import call

BASE_URL='https://www.bing.com'

def create_cache_dir():
    dir = '%s/.cache/bing' % (os.getenv("HOME"))
    if not os.path.exists(dir):
        os.mkdir(dir)
    return dir

def download_file(path,url):
    r = get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    return path
def get(route,stream=False):
    url = "%s%s" % (BASE_URL,route)
    print(url)
    return  requests.get(url,stream=stream)

junk = get('/HPImageArchive.aspx?format=js&n=1&nc=%s' % (time.time()))

path = '%s/wallpaper.jpg' % (create_cache_dir())
print("Saving wallpaper: " + download_file(path,"%s" % (junk.json()['images'][0]['url'])))

call(['gsettings' ,'set', 'org.gnome.desktop.background', 'picture-uri', ('file://%s'  % (path))])