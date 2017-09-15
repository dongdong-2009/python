#!/usr/bin/python

if __name__ == '__main__':
	list1 = [1,2,3,4,5,6,7,8,9,10]
	list2 = [num for num in list1 if num % 2 == 0]
	#print(list2)

	for i in (num for num in list1 if num % 2 == 0):
		print(i,"是偶数")
