#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import locale

def get_code_files(root_path):
    for path in os.walk(root_path):
        root, dirs, files = path
        for file in files:
            if (file.endswith('.py')):
                yield os.path.join(root, file)
    
def stat_files(root_path):
    code_count, cmt_count, blank_count  = 0, 0, 0
    
    for code_path in get_code_files(root_path):
        encoding = locale.getpreferredencoding(code_path)
        with open(code_path, 'r', encoding=encoding) as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    blank_count += 1
                elif line.startswith('#'):
                    cmt_count += 1
                else:
                    code_count += 1
        
    total = code_count + cmt_count + blank_count
    return total, code_count, cmt_count, blank_count

if __name__ == '__main__':
    result = stat_files('../')
    print('Total:{total} lines\n'
          'Code:{code} lines\n'
          'Comment:{cmt} lines\n'
          'Blank:{blank} lines'.format(
          total = result[0],
          code = result[1],
          cmt = result[2],
          blank = result[3]
          )
    )