#!/usr/bin/python

#使用列表实现队列结构

import os

list1 = []

def in_queue(val):
	list1.append(val)

def out_queue():
	if(len(list1) >= 0):
		return list1.pop(0)
	else:
		return None
#list1.remove(list1[0])

def show_queue():
	print(list1)

if(__name__ == "__main__"):
	while True:
		os.system('clear')
		print("\33[32m功能菜单:\33[0m")
		print("\tin:入队\tout:出队\tshow:显示队列\tquit：退出\n\n\n")
		op = input("请输入功能按回车结束：")
		
		if(op == "in"):
			val = input("请输入要入队的元素：")
			in_queue(val)
		elif(op == "out"):	
			val = out_queue()
			print("出队元素：",val)
			input("按任意键继续...")
		elif(op == "show"):
			show_queue()
			input("按任意键继续...")
		elif(op == "quit"):
			break;
