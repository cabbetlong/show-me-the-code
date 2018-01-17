#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from PIL import ImageDraw, ImageFont, Image

def draw_num(pic_path, n):
    white = (255, 255, 255)
    red = (255, 0, 0)
    
    with Image.open(pic_path) as img:
        # set position
        w, h = img.size
        text_position = (w-73, 33)
        elps_posinton = [w-90, 30, w-30, 90]
        
        # set font and it's size
        font = ImageFont.truetype('arial.ttf', 50)
        
        # draw ellipse and text
        draw = ImageDraw.Draw(img)
        draw.ellipse(elps_posinton, red)
        text = str(random.randrange(1, 9, 1))
        draw.text(text_position, text, white, font=font)
        
        # save modified image.
        img.save('./result_{n}.jpg'.format(n=n))
        
if __name__ == '__main__':
    # test
    draw_num('./1.jpeg', 1)
    draw_num('./2.jpg', 2)