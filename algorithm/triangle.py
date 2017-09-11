#!/usr/bin/python
# -*- coding: utf-8 -*-

def triangel(n):
	L=[1]                                                                 #定义一个list[1]
	while True:
#_len = len(L)
#for x in range(_len):
#	print("x = %d" %(x))
		yield  L                                                         #打印出该list
		L=[L[x]+L[x+1] for x in range(len(L)-1)]        #计算下一行中间的值（除去两边的1）
		L.insert(0,1)                                                 #在开头插入1
		L.append(1)                                                 #在结尾添加1
		if len(L)>10:                                                 #仅输出10行
			break

if __name__ == '__main__':
	a = triangel(10)
	for i in a:
		print(i)
