#!/usr/bin/python

from PIL import Image

if __name__ == '__main__':
	im = Image.open('img/1.jpg')
	print(im.format,im.size,im.mode)
	#im.save('img/1_save.jpg', 'JPEG')