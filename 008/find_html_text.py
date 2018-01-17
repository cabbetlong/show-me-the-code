#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests # get html by url
from bs4 import BeautifulSoup # parse html

def get_html(url):
    r = requests.get(url)
    return r.text
    
def find_html_text(html, text_tag='body'):
    soup = BeautifulSoup(html, "lxml")
    return str(soup(text_tag))

if __name__ == '__main__':
    html = get_html('https://github.com/Yixiaohan/show-me-the-code')
    text = find_html_text(html, text_tag='article') 
    print(text)