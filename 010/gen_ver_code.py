#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

w, h = 50,50 # size of each char is 50*50
font_size = 36

def _random_chars(n):
    for __ in range(n):
        yield random.choice(string.ascii_letters + string.digits) #'a-zA-Z' + '0-9'
        
def _random_RGB(start, end):
    while True:
        yield random.randint(start, end), random.randint(start, end), random.randint(start, end)
        
def gen_background(n):
    img_size = (w * n, h)
    img = Image.new('RGB', img_size, (255,255,255))
    
    draw = ImageDraw.Draw(img)
    for x in range(img.width):
        for y in range(img.height):
            draw.point((x, y), next(_random_RGB(64, 255)))
            
    return img

def add_text(img, text):
    font = ImageFont.truetype('arial.ttf', font_size)
    draw = ImageDraw.Draw(img)
    for idx, ch in enumerate(text):
        pos = (idx*w+10, 10)
        fill = next(_random_RGB(32, 127))
        draw.text(pos, ch, fill, font = font)

    return img

def gen_ver_code(n):
    # generate background
    img = gen_background(n)
    # add text to background
    text = ''.join(_random_chars(n))
    add_text(img, text)
    # blur img
    img = img.filter(ImageFilter.BLUR)

    return img, text

if __name__ == '__main__':
    img, text = gen_ver_code(4)
    print(text)
    img.show()