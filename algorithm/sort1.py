#!/bin/usr/python
# -*- coding: utf-8 -*-

def by_name(t):
	return (str.lower(t[0]))

def by_score(t):
	return t[1]

if __name__ == "__main__":
	L = [('Bob', 75), ('Adam', 92), ('dart', 66), ('Lisa', 88)]
#	L2 = sorted(L)
#	L2 = sorted(L,key=by_name)
	L2 = sorted(L,key=by_score,reverse=True)
	print(L2)
