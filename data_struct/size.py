#!/usr/bin/python

import sys

if(__name__ == "__main__"):
	a = 10
	#b = 10L
	c = 3.14
	d = 3 + 4j
	e = True
	print("int :",sys.getsizeof(a))
	#print(sys.getsizeof(b))
	print("float :",sys.getsizeof(c))
	print("complex :",sys.getsizeof(d))
	print("bool :",sys.getsizeof(e))
	print("2^3 =",2**3)	#python指数
	#print("int_max :",sys.maxfloat) #会报错
	print("hex(10) =",hex(10))
	print("sys.version = ",sys.version)
	print("sys.hexversion = ",sys.hexversion)
	print("sys.float_info =",sys.float_info)
	print("type(10):",type(10))
	print("type(10+10j):",type(10+10j))
