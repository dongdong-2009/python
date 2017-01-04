#!/usr/bin/python

#使用列表实现堆栈结构
import os

list1 = []

def push(val):
	list1.append(val)

def pop():
	list1.pop()

def show():
	print("当前列表：",list1)

if(__name__ == "__main__"):
	while True:
		os.system('clear')
		print("功能列表：\n")
		print("\tp:push")
		print("\to:pop")
		print("\ts:show")
		print("\tq:quit")
		op = input("请输入您想要的操作:")
		if(op == "q"):
			break
		elif(op == "p"):
			val = input("请输入要入栈的对象：")
			push(val)
		elif(op == "o"):
			pop()
		elif(op == "s"):
			show()
			input("按任意键继续")
	
