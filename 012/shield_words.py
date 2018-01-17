#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def read_words(path):
    with open(path, 'r') as file:
        return list(map(lambda x:x.strip(), file.readlines()))
        
def display():
    words = read_words('./filtered_words.txt')
    while True:
        usr_in = input('Please input a word:')
        if usr_in == 'exit':
            return
        else:
            for s in words:
                r = '*' * len(s) * (s in usr_in) or r
                usr_in = usr_in.replace(s, r)
            print(usr_in)
        
if __name__ == '__main__':
    display()