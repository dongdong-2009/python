#!/usr/bin/python
#-*- coding:utf-8 -*-

'a test module'

__author__ = 'Akon'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print("Hello world!")
	elif len(args) == 2:
		print("Hello %s" % args[1])
	else:
		print("Args is too maney")

if __name__ == '__main__':	
	test()
else:
	num = 1
	_num = 2
	__num = 3
	print("********************************************************")
	print("[M]Author is %s,module_name is %s" % (__author__,__name__))
	print("********************************************************")