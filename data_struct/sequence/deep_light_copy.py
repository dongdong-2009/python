#!/usr/bin/python

import copy

if(__name__ == "__main__"):
	"""
		浅拷贝
		child2和child3同时指向child1指向的内存单元
		当修改child2[0]时由于元组不能修改，所以child2指向新的内存单元
		child3修改列表元素，所以child3仍然指向child1
	"""
	print("=========浅拷贝==========\n")
	child1 = [("age","height"),[10,120]]
	child2 = list(child1)
	child3 = list(child1)
	child2[0] = ("age","height","weight")
	child3[1].append(38) 
	print("child1 = ",child1,"\nchild2 = ",child2,"\nchild3 =",child3)
	print(id(child1))
	print(id(child2))
	print(id(child3))

	"""
		深拷贝
			元组仍然指向相同地址
			列表指向不同地址
	"""
	print("=========深拷贝==========\n")
	child1 = [("age","height"),[10,120]]
	child2 = copy.deepcopy(child1)
	print("child1:",id(child1),"\tchild1[1]:",id(child1[1]),"\tchild1[0]:",id(child1[0]))
	print("child2:",id(child2),"\tchild2[1]:",id(child2[1]),"\tchild2[0]:",id(child2[0]))

	'''
	'''
