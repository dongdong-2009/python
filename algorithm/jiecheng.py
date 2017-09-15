#!/usr/bin/python

from functools import reduce

def jiecheng(n):
	return reduce(lambda x,y:x * y,range(1,n+1))

if __name__ == "__main__":
	print(jiecheng(5))
