#!/usr/bin/python

from functools import reduce

def add(x,y):
	if(type(x) == int and type(y) == int):
		return x + y
	else:
		print("Args is valied!!!")

if(__name__ == "__main__"):
	print(reduce(add,list(range(101))))
