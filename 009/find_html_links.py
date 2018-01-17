#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests

def get_html(url):
    r = requests.get(url)
    return r.text
    
def find_html_links(html):
    re_url = re.compile('\"https?://[^\s]*\"')
    links = re_url.findall(html)

    return set(map(lambda x:x.strip('"'), links)) # use set to remove duplicates

if __name__ == '__main__':
    html = get_html('https://github.com/Yixiaohan/show-me-the-code')
    links = find_html_links(html)
    print(links)