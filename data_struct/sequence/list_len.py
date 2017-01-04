#!/usr/bin/python

#统计列表中元素的个数
import sys

def list_count(_list):
	count = 0
	for i in _list:
		if(isinstance(i,list)):
			print(i)
			count += len(i)
	return count

if(__name__ == "__main__"):
	print("脚本名：",sys.argv[0])
	for i in range(1,len(sys.argv)):
		print("参数",i,sys.argv[i])	
	name = "mkk"
	score1 = [90,90,90]
	score2 = [80,80,80]
	print(list_count([name,score1,score2]))

#命令行传惨会当作字符串处理
#list1 = sys.argv[1]
#print(list_count(list1))
	
