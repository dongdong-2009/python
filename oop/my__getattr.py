#!/usr/bin/python

'''
	动态URL实现
'''

class Chain(object):
	def __init__(self,path=''):
		print("path:%s"%(path))
		self._path = path

	def __getattr__(self,path):
		return Chain('%s/%s'%(self._path,path))
	
	def __str__(self):
		return self._path

	__repr__ = __str__

if(__name__ == '__main__'):
	print(Chain().root.home.mkk.python)
