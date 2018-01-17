#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ast
import xlwt
from collections import Iterable

def read_stus_info(path):
    with open(path, 'r') as file:
        content = file.read()
        # a safe version of eval(), https://stackoverflow.com/questions/13675942/converting-string-to-dict
        return ast.literal_eval(content)
        
def trav_info(info):
    for key, value in info.items():
        row = int(key)-1
        yield row, 0, key
        for idx, item in enumerate(value):
            yield row, idx+1, item

def write2xls(path, stus_info):
    stu_xls = xlwt.Workbook()
    stu_ws = stu_xls.add_sheet('Students')
    for item in stus_info:
        stu_ws.write(item[0], item[1], item[2])
    stu_xls.save(path)

if __name__ == '__main__':
    stus_info = read_stus_info('./students.txt')
    write2xls('./students.xls', trav_info(stus_info))
