#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def read_words(path):
    with open(path, 'r') as file:
        return [s.strip() for s in file.readlines()]
            
def display():
    words = read_words('./filtered_words.txt')
    while True:
        usr_in = input('Please input a word:')
        if usr_in == 'exit':
            return
        elif usr_in in words:
            print('Freedom')
        else:
            print('Human Rights')
        
if __name__ == '__main__':
    display()