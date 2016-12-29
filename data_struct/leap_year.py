#!/usr/bin/python


if(__name__ == "__main__"):
	#由于input返回的类型为字符串，所以需要抢转
	year = int(input("Please input a year :"))
	if(year % 400 == 0):
		print("%d is leap year" % year)
	elif(year % 4 == 0 and year % 100 != 0):
		print("%d year is leap year" % year)
	else:
		print("%d year is not leap year" % year)
