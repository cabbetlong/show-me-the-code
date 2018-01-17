#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from PIL import Image

i5_w = 640
i5_h = 1136

def zoom_pic(path, pic_exts):
    files = os.listdir(path)
    # Get pictrues in path
    pic_files = filter(lambda x:any(os.path.isfile(x) and x.endswith(ext) for ext in pic_exts), files)

    for pic_file in pic_files:
        with Image.open(pic_file) as img:
            w, h = img.size
            w = (w < i5_w) * w or i5_w
            h = (h < i5_h) * h or i5_h
            
            des_img = img.resize((w, h))
            
            result_name = '{name}_i5.{ext}'.format(name=pic_file.split('.')[0], ext=pic_file.split('.')[1])
            des_img.save(result_name)

if __name__ == '__main__':
    pic_ext = ['.jpg', '.png']
    zoom_pic(r'./', pic_ext)