#!/usr/bin/python3
# -*- coding:utf-8 -*-

from PIL import Image

if __name__ == "__main__":
    im = Image.open('1.jpg')
    w, h = im.size
    print('Original image size: %sx%s' % (w, h))
    im.thumbnail((w // 2, h // 2))
    print('Resize image to: %sx%s' % (w // 2, h // 2))
    im.save('thumbnail.jpg', 'jpeg')