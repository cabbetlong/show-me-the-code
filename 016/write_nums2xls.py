#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ast
import xlwt

def read_city(path):
    with open(path, 'r') as file:
        content = file.read()
        return ast.literal_eval(content)
        
def write_city2xls(lst):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('numbers')
   
    for row, nums in enumerate(lst):
        for col, value in enumerate(nums):
            ws.write(row, col, value)
       
    wb.save('numbers.xls')
        
if __name__ == '__main__':
    lst = read_city('./numbers.txt')
    write_city2xls(lst)