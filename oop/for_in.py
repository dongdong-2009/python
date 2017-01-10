#!/usr/bin/python

'''
一个类想要实现for...in循环，类似list和tuple，就必须要实现一个__iter__方法，该方法返回一个迭代对象
然后python的for循环就会不断调用该迭代对象的__next__方法拿到循环的下一个值，知道遇到StopIteration错误时退出循环
实现案例：翡波那契数列
'''

import time

class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1

	def __str__(self):
		return '恭喜您创建了一个Fib类'

	__repr__ = __str__

	def __iter__(self):
		return self

	def __next__(self):
		self.a,self.b = self.b,self.a+self.b
		if(self.a > 100):
			return 'err'
			'''return StopIteration();'''
		return self.a

if(__name__ == "__main__"):
	for n in Fib():
		time.sleep(0.1)
		if(n == 'err'):
			print("=========end===========")
			break;
		print(n)
	'''
	fib = Fib()
	while True:
		time.sleep(0.1)
		print(fib.__next__())
'''
