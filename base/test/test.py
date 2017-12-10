#!/usr/bin/python
#-*-coding:utf-8-*-

'测试python基础特性'

__author__ = 'akon'
def test_func():
	print("call test func")

#默认参数每次被调用的时候都会被记住上次的值
def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

#加*代表是可变参数
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

#关键字参数会当做dict被传入,可以传入任意的dict
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

#命名关键字参数，*为占位符，后面的参数只能是限定的city
def person1(name,age,*,city="bejing"):
	print(name,age,city)

if __name__ == "__main__":
	print("call test")
	person1('akon','20',city="bejing")
else:
	print("\n__name__ = "+__name__+",test module is refed\n")
