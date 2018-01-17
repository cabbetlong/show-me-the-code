#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import shutil
from bs4 import BeautifulSoup
import time
import aiohttp
import asyncio


def get_html(url):
    r = requests.get(url)
    return r.text


def find_pic_links(html):
    soup = BeautifulSoup(html, 'lxml')
    imgs = soup.find_all('img', attrs={'class': 'BDE_Image'})
    for img in imgs:
        yield img['src']


async def download_img(url, save_path):
    async with aiohttp.request('GET', url) as r:
        data = await r.read()
        print('Downloading: ', url[url.rfind('/'):])
        if data:
            with open(save_path, 'wb') as out_file:
                out_file.write(data)


if __name__ == '__main__':
    start = time.time()

    html = get_html('http://tieba.baidu.com/p/2166231880')
    pic_urls = find_pic_links(html)

    sema = asyncio.Semaphore(5) # 最大协程数
    event_loop = asyncio.get_event_loop()
    tasks = [download_img(pic_url,
                          './{name}{ext}'.format(name=idx, ext=pic_url[pic_url.rindex('.'):]))
             for idx, pic_url in enumerate(pic_urls)]
    event_loop.run_until_complete(asyncio.gather(*tasks))

    print('cost: {}s'.format(time.time() - start))
    # out:
    # cost: 1.8681070804595947s