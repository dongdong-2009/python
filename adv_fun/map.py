#!/usr/bin/python

def square(x):
	if(type(x) == int):
		return (x)*(x)
	else:
		print("Args is valied!!!")

if(__name__ == "__main__"):
	print(list(map(square,list(range(10)))))
