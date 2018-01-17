#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import shutil
from bs4 import BeautifulSoup
import time

def get_html(url):
    r = requests.get(url)
    return r.text
    
def find_pic_links(html):
    soup = BeautifulSoup(html, 'lxml')
    imgs = soup.find_all('img', attrs={'class':'BDE_Image'})
    for img in imgs:
        yield img['src']
            
def download_img(url, save_path):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(save_path, 'wb') as out_file:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, out_file)

if __name__ == '__main__':
    start = time.time()
    html = get_html('http://tieba.baidu.com/p/2166231880')
    pic_urls = find_pic_links(html)

    for idx, pic_url in enumerate(pic_urls):
        save_path = './{name}{ext}'.format(name=idx, ext=pic_url[pic_url.rindex('.'):])
        download_img(pic_url, save_path)
        
    print('cost: {}s'.format(time.time() - start))
    # out:
    # cost: 43.939513206481934s