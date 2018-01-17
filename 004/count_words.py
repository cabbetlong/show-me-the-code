#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def count_words(path):
    with open(path, 'r') as file:
        return len(re.findall(r'[\w\-\_\.\']+', file.read()))
        
if __name__ == '__main__':
    print(count_words('./text.txt'))