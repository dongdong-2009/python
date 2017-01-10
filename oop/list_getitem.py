#!/usr/bin/python

'''
	__getitem__方法实现list的下标取值
'''

import time

class Fib(object):
	def __str__(self):
		return '恭喜创建了Fib实例'

	def __getitem__(self,n):
		if(isinstance(n,int)):
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a
		if(isinstance(n,slice)):
			start = n.start
			stop = n.stop
			print("start = %d,stop = %d"%(start,stop))
			if start is None:
				start = 0
			a,b = 1,1
			L = []
			for x in range(stop):
				if(x >= start):
					L.append(a)
				a,b = b,a+b
			return L

if(__name__ == '__main__'):
	f = Fib()
	for n in range(1,10,2):
		print("f[%d]:%d"%(n,f[n]))
	for n in f:
		time.sleep(0.1)
		print(n)
