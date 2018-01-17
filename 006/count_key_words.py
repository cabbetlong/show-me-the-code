#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import re

def count_key_words(key_words):
    contents = []
    
    for file_name in glob.glob('*.txt'):
        with open(file_name, 'r') as file:
            contents.append(file.read())
            
    str = ''.join(contents).lower()
    return dict(map(lambda x:(x, len(re.findall(x, str))), key_words))
    
if __name__ == '__main__':
    print(count_key_words(['byte', 'type']))