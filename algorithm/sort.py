#!/bin/usr/python

import math

if __name__ == "__main__":
	print(sorted([10,-10,5,4,19]))
	print(sorted([10,-10,5,4,19],key = abs))
	print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))		#忽略大小写排序
	print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse = True))		#忽略大小写反向排序
