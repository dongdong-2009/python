#!/usr/bin/python

import random

if(__name__ == "__main__"):
	num = random.randint(0,15)
	i = 0
	s = ""

	while(i < 4):
		if(num >> i & 0x01):
			s = '1' + s
		else:
			s = '0' + s
		i = i + 1
	print("%d : %s\n" % (num,s))
