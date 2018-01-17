#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ast
import xlwt

def read_city(path):
    with open(path, 'r') as file:
        content = file.read()
        return ast.literal_eval(content)
       
def write_city2xls(dic):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('City')
   
    for key, value in dic.items():
        row = int(key) - 1
        ws.write(row, 0, key)
        ws.write(row, 1, value)
       
    wb.save('city.xls')
       
if __name__ == '__main__':
    dic = read_city(r'.\city.txt')
    write_city2xls(dic)